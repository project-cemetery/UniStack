# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-03 06:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20170331_0900'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='название')),
                ('cost', models.IntegerField(verbose_name='стоимость за семестр')),
                ('percent', models.FloatField(verbose_name='комиссия')),
                ('expiration_date', models.DateField(verbose_name='дата окончания обновления')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.City')),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Exam')),
            ],
            options={
                'verbose_name_plural': 'подготовительные курсы',
                'verbose_name': 'подготовительные курсы',
            },
        ),
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=255, verbose_name='название'),
        ),
        migrations.AlterField(
            model_name='department',
            name='site',
            field=models.URLField(verbose_name='сайт'),
        ),
        migrations.AlterField(
            model_name='subdivision',
            name='abbr',
            field=models.CharField(max_length=127, verbose_name='аббревиатура'),
        ),
        migrations.AlterField(
            model_name='subdivision',
            name='name',
            field=models.CharField(max_length=255, verbose_name='название'),
        ),
        migrations.AlterField(
            model_name='subdivision',
            name='site',
            field=models.URLField(verbose_name='сайт'),
        ),
        migrations.AlterField(
            model_name='university',
            name='abbr',
            field=models.CharField(max_length=127, verbose_name='аббревиатура'),
        ),
        migrations.AlterField(
            model_name='university',
            name='name',
            field=models.CharField(max_length=255, verbose_name='название'),
        ),
        migrations.AlterField(
            model_name='university',
            name='site',
            field=models.URLField(verbose_name='сайт'),
        ),
    ]
