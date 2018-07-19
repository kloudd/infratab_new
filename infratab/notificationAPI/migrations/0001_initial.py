# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Days',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('days', models.CharField(choices=[('1', 'Monday'), ('2', 'Tuesday'), ('3', 'Wednesday'), ('4', 'Thursday'), ('5', 'Friday'), ('6', 'Saturday'), ('7', 'Sunday')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('phone_no', models.IntegerField(default='', blank=True)),
                ('email', models.CharField(default='', max_length=100, blank=True)),
                ('date', models.DateTimeField()),
                ('is_recurring', models.BooleanField(default=True)),
                ('last_date', models.DateTimeField()),
                ('is_week_day', models.BooleanField(default=True)),
                ('days', models.ManyToManyField(to='notificationAPI.Days', blank=True)),
            ],
        ),
    ]
