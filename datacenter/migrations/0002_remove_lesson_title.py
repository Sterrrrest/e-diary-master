# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-06-26 19:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datacenter', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='title',
        ),
    ]
