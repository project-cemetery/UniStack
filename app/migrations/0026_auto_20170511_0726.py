# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-11 07:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_auto_20170510_1035'),
    ]

    operations = [
        migrations.DeleteModel(
            name='NamedLink',
        ),
        migrations.AddField(
            model_name='university',
            name='foundation_year',
            field=models.IntegerField(blank=True, null=True, verbose_name='год основания'),
        ),
    ]
