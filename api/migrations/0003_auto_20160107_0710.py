# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-07 07:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20160107_0709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bucketlist',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='bucketlist',
            name='date_modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='date_modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
