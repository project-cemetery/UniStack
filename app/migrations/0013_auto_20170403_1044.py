# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-03 10:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_sociallink'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Specialty',
            new_name='Speciality',
        ),
        migrations.RenameModel(
            old_name='SpecialtyGroup',
            new_name='SpecialityGroup',
        ),
    ]