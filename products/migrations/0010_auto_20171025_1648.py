# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 11:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20171025_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(blank=True, max_length=36, null=True),
        ),
    ]
