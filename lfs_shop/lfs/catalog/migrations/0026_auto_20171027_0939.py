# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-10-27 11:39
from __future__ import unicode_literals

from django.db import migrations
import lfs.cloud_storage.cloud_fields


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0025_auto_20171027_0753'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='cloud_image',
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=lfs.cloud_storage.cloud_fields.CloudImageField(blank=True, null=True, upload_to=b'images', verbose_name='Image'),
        ),
    ]
