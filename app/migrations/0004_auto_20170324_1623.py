# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-24 16:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20170324_1328'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainingDirection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='название')),
                ('url', models.URLField()),
                ('description', models.TextField(blank=True, null=True, verbose_name='описание')),
                ('intro', models.TextField(blank=True, null=True, verbose_name='интро')),
            ],
            options={
                'verbose_name': 'направление подготовки',
                'verbose_name_plural': 'направления подготовки',
            },
        ),
        migrations.CreateModel(
            name='TrainingDirectionGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='название')),
            ],
            options={
                'verbose_name': 'группа направлений подготовки',
                'verbose_name_plural': 'группы направлений подготовки',
            },
        ),
        migrations.AddField(
            model_name='trainingdirection',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.TrainingDirectionGroup'),
        ),
    ]
