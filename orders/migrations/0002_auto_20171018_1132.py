# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-18 06:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductsInOrder',
            new_name='ProductInOrder',
        ),
    ]
