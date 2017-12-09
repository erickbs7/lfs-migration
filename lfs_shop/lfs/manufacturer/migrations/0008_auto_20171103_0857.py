# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-03 10:57
from __future__ import unicode_literals

from django.db import migrations
import lfs.cloud_storage.cloud_fields


class Migration(migrations.Migration):

    dependencies = [
        ('manufacturer', '0007_auto_20171026_1010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manufacturer',
            name='image',
            field=lfs.cloud_storage.cloud_fields.CloudImageField(blank=True, null=True, sizes=((60, 60), (100, 100), (200, 200), (400, 400)), upload_to=b'images', verbose_name='Image'),
        ),
    ]
