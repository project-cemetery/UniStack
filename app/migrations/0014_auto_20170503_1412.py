# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-03 14:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20170403_1044'),
    ]

    operations = [
        migrations.CreateModel(
            name='NamedLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='название')),
            ],
            options={
                'verbose_name': 'именованая ссылка',
                'verbose_name_plural': 'именованные ссылки',
            },
        ),
        migrations.AddField(
            model_name='university',
            name='address',
            field=models.CharField(blank=True, max_length=511, null=True, verbose_name='адрес главного корпуса'),
        ),
        migrations.AddField(
            model_name='university',
            name='social_links',
            field=models.ManyToManyField(to='app.NamedLink'),
        ),
    ]
