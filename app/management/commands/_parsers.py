from app.models import TrainingDirectionGroup, TrainingDirection
from app.models import Country, Region, City
from django.core.exceptions import ObjectDoesNotExist

from lxml.html import fromstring
from lxml import *
import requests

import os

import gspread
from oauth2client.service_account import ServiceAccountCredentials


class Parser:
    def parse(self):
        pass


class GoogleSheetsParser(Parser):
    def __get_credentials(self):
        scope = ['https://spreadsheets.google.com/feeds']

        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            'app/management/commands/credentials/uni-stack-8109d2248632.json',
            scope)

        return credentials

    def get_worksheet(self, key):
        credentials = self.__get_credentials()

        gc = gspread.authorize(credentials)
        worksheet = gc.open_by_key(key).sheet1

        return worksheet


class GoogleSheetsCitiesParser(GoogleSheetsParser):
    country_count = 0
    region_count = 0
    city_count = 0

    def parse(self):
        worksheet = GoogleSheetsParser.get_worksheet(self, '1Mp9r7CNxVnKip-tLAFpbGp4K_MY2iUrbrBOQBcsKLVE')

        i = 2
        while True:
            values_list = worksheet.row_values(i)
            i += 1

            if not values_list[0]:
                break

            try:
                country = Country.objects.get(
                    name=values_list[4]
                )
            except ObjectDoesNotExist:
                country = Country(
                    name=values_list[4]
                )
                self.country_count += 1
                country.save()

            try:
                region = Region.objects.get(
                    name=values_list[1]
                )
            except ObjectDoesNotExist:
                region = Region(
                    name=values_list[1],
                    country=country
                )
                self.region_count += 1
                region.save()

            try:
                city = City.objects.get(
                    name=values_list[0]
                )
            except ObjectDoesNotExist:
                city = City(
                    name=values_list[0],
                    lat=values_list[2],
                    lon=values_list[3],
                    region=region
                )
                self.city_count += 1
                city.save()

        return [
            'New Countries: ' + str(self.country_count),
            'New Regions: ' + str(self.region_count),
            'New Cities: ' + str(self.city_count)
        ]


class FgosTrainingDirectionParser(Parser):
    BASE_URL = 'http://www.edu.ru/'

    direction_count = 0
    group_count = 0

    def __parse_direction(self, direction):
        request = requests.get(direction.url)

        dom = fromstring(request.text)
        table = dom.xpath('//table')[3]
        for row in table:
            for cell in row:
                if cell.get('class') == 'tdcont':
                    p_counter = 0
                    h1_counter = 0
                    for item in cell:
                        if item.tag == 'h1':
                            h1_counter += 1
                            if h1_counter == 3:
                                t = item.text.split('(')[1].replace(')', '')
                                if t.startswith('маг'):
                                    return None
                        if item.tag == 'p':
                            p_counter += 1
                            if item.text_content() != '':
                                direction.description = item.text_content()
                                break

        direction.code = direction.url.split('fgos.')[1].split('/st.')[0]
        self.direction_count += 1

        return direction

    def __parse_group(self, relative_url, group):
        request = requests.get(self.BASE_URL + relative_url)

        dom = fromstring(request.text)
        table = dom.xpath('//table')[4]

        direction_array = []
        for row in table:
            for cell in row:
                if cell.get('width') != '15':
                    for item in cell:
                        if item.tag == 'a':
                            try:
                                direction = TrainingDirection.objects.get(
                                    name=item.text
                                )
                            except ObjectDoesNotExist:
                                direction = TrainingDirection(
                                    name=item.text
                                )
                                direction.url = self.base_url + item.get('href')
                                direction.group = group
                                direction = self.__parse_direction(direction)
                            if direction:
                                direction.save()
                                direction_array.append(direction)

        return direction_array

    def parse(self):
        request = requests.get(self.BASE_URL + '/abitur/act.6/index.php')

        dom = fromstring(request.text)
        table = dom.xpath('//table')[4]

        group_array = []
        direction_array = []
        for row in table:
            for cell in row:
                for link in cell:
                    try:
                        group = TrainingDirectionGroup.objects.get(
                            name=link.text
                        )
                    except ObjectDoesNotExist:
                        group = TrainingDirectionGroup(
                            name=link.text
                        )
                        self.group_count += 1
                    group.save()
                    direction_array += self.__parse_group(link.get('href'), group)
                    group_array.append(group)

        result = [
            'New Training Direction Groups: ' + str(self.group_count),
            'New Training Directions: ' + str(self.direction_count),
        ]

        return result
