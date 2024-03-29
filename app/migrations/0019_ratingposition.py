# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-10 09:06
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_auto_20170510_0903'),
    ]

    operations = [
        migrations.CreateModel(
            name='RatingPosition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField(verbose_name='позиция в рейтинге')),
                ('rating', models.ManyToManyField(related_name='рейтинг', to='app.Rating')),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.University')),
            ],
        ),
    ]
