# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-15 06:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corrfeed', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='reason',
            field=models.CharField(choices=[('Similiar', "It's similiar to another"), ('Abusive', 'The poster made use of abusive language'), ('Files', 'The evidences attched is not tenable/appropriate'), ('Sensitive', 'It contains sensitive information'), ('Rules', 'It contravenes one of the other rules'), ('Other', 'Other,Pls specify')], default='Rules', max_length=10),
        ),
    ]