# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-02 12:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_auto_20160502_1230'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='instructions',
        ),
        migrations.AddField(
            model_name='recipeingredients',
            name='instructions',
            field=models.CharField(default='', max_length=100),
        ),
    ]