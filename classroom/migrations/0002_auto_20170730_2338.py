# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-31 06:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='class_list',
            field=models.TextField(),
        ),
    ]
