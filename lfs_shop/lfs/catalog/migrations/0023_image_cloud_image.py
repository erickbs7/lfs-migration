# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-10-26 22:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0022_auto_20171026_2032'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='cloud_image',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
