# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-10-25 10:34
from __future__ import unicode_literals

from django.db import migrations
import lfs.cloud_storage.cloud_fields


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_auto_20171025_0824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=lfs.cloud_storage.cloud_fields.CloudImageField(max_length=250, null=True),
        ),
    ]
