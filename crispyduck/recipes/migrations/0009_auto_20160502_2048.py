# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-02 20:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0008_auto_20160502_2046'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RecipeInstructions',
            new_name='RecipeInstruction',
        ),
    ]