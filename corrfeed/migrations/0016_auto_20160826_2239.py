# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-26 21:39
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corrfeed', '0015_auto_20160825_2255'),
    ]

    operations = [
        migrations.AddField(
            model_name='authority',
            name='pub_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, max_length=16, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]