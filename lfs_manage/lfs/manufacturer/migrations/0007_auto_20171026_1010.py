# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-10-26 12:10
from __future__ import unicode_literals

from django.db import migrations
import lfs.core.fields.thumbs


class Migration(migrations.Migration):

    dependencies = [
        ('manufacturer', '0006_auto_20171026_0950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manufacturer',
            name='image',
            field=lfs.core.fields.thumbs.ImageWithThumbsField(blank=True, null=True, sizes=((60, 60), (100, 100), (200, 200), (400, 400)), upload_to=b'images', verbose_name='Image'),
        ),
    ]
