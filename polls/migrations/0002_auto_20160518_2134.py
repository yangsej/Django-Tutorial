# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-18 12:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='put_date',
            new_name='pub_date',
        ),
    ]