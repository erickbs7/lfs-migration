# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-28 01:22
from __future__ import unicode_literals

from django.db import migrations
import lfs.cloud_storage.cloud_fields


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0028_auto_20171102_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=lfs.cloud_storage.cloud_fields.CloudImageField(blank=True, null=True, sizes=((60, 60), (100, 100), (200, 200), (300, 300), (400, 400), (600, 600)), upload_to=b'images', verbose_name='Image'),
        ),
    ]
