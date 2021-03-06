# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-25 07:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0003_auto_20190515_0820'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimetableDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_of_week_start', models.CharField(choices=[('\u041f\u043d', '\u041f\u043e\u043d\u0435\u0434\u0435\u043b\u044c\u043d\u0438\u043a'), ('\u0412\u0442', '\u0412\u0442\u043e\u0440\u043d\u0438\u043a'), ('\u0421\u0440', '\u0421\u0440\u0435\u0434\u0430'), ('\u0427\u0442', '\u0427\u0435\u0442\u0432\u0435\u0440\u0433'), ('\u041f\u0442', '\u041f\u044f\u0442\u043d\u0438\u0446\u0430'), ('\u0421\u0431', '\u0421\u0443\u0431\u0431\u043e\u0442\u0430'), ('\u0412\u0441', '\u0412\u043e\u0441\u043a\u0440\u0435\u0441\u0435\u043d\u044c\u0435')], max_length=14, verbose_name='\u0421 \u0434\u043d\u044f \u043d\u0435\u0434\u0435\u043b\u0438')),
                ('day_of_week_end', models.CharField(choices=[('\u041f\u043d', '\u041f\u043e\u043d\u0435\u0434\u0435\u043b\u044c\u043d\u0438\u043a'), ('\u0412\u0442', '\u0412\u0442\u043e\u0440\u043d\u0438\u043a'), ('\u0421\u0440', '\u0421\u0440\u0435\u0434\u0430'), ('\u0427\u0442', '\u0427\u0435\u0442\u0432\u0435\u0440\u0433'), ('\u041f\u0442', '\u041f\u044f\u0442\u043d\u0438\u0446\u0430'), ('\u0421\u0431', '\u0421\u0443\u0431\u0431\u043e\u0442\u0430'), ('\u0412\u0441', '\u0412\u043e\u0441\u043a\u0440\u0435\u0441\u0435\u043d\u044c\u0435')], max_length=14, verbose_name='\u041f\u043e \u0434\u0435\u043d\u044c \u043d\u0435\u0434\u0435\u043b\u0438')),
                ('start_time1', models.TimeField(verbose_name='\u041d\u0430\u0447\u0430\u043b\u043e 1 \u0441\u043c\u0435\u043d\u044b')),
                ('end_time1', models.TimeField(verbose_name='\u041e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u0435 1 \u0441\u043c\u0435\u043d\u044b')),
                ('lunch_start1', models.TimeField(blank=True, null=True, verbose_name='\u041d\u0430\u0447\u0430\u043b\u043e \u043e\u0431\u0435\u0434\u0430 1 \u0441\u043c\u0435\u043d\u044b')),
                ('lunch_end1', models.TimeField(blank=True, null=True, verbose_name='\u041e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u0435 \u043e\u0431\u0435\u0434\u0430 1 \u0441\u043c\u0435\u043d\u044b')),
                ('start_time2', models.TimeField(verbose_name='\u041d\u0430\u0447\u0430\u043b\u043e 2 \u0441\u043c\u0435\u043d\u044b')),
                ('end_time2', models.TimeField(verbose_name='\u041e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u0435 2 \u0441\u043c\u0435\u043d\u044b')),
                ('lunch_start2', models.TimeField(blank=True, null=True, verbose_name='\u041d\u0430\u0447\u0430\u043b\u043e \u043e\u0431\u0435\u0434\u0430 2 \u0441\u043c\u0435\u043d\u044b')),
                ('lunch_end2', models.TimeField(blank=True, null=True, verbose_name='\u041e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u0435 \u043e\u0431\u0435\u0434\u0430 2 \u0441\u043c\u0435\u043d\u044b')),
                ('start_time3', models.TimeField(verbose_name='\u041d\u0430\u0447\u0430\u043b\u043e 3 \u0441\u043c\u0435\u043d\u044b')),
                ('end_time3', models.TimeField(verbose_name='\u041e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u0435 3 \u0441\u043c\u0435\u043d\u044b')),
                ('lunch_start3', models.TimeField(blank=True, null=True, verbose_name='\u041d\u0430\u0447\u0430\u043b\u043e \u043e\u0431\u0435\u0434\u0430 3 \u0441\u043c\u0435\u043d\u044b')),
                ('lunch_end3', models.TimeField(blank=True, null=True, verbose_name='\u041e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u0435 \u043e\u0431\u0435\u0434\u0430 3 \u0441\u043c\u0435\u043d\u044b')),
            ],
        ),
        migrations.AlterField(
            model_name='equipment',
            name='description',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435'),
        ),
    ]
