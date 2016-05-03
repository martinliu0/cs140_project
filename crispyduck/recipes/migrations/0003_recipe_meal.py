# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-02 11:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_auto_20160502_1136'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='meal',
            field=models.CharField(choices=[('BR', 'Breakfast'), ('LN', 'Lunch'), ('DN', 'Dinner'), ('DS', 'Dessert'), ('SN', 'Snack')], default='LN', max_length=2),
        ),
    ]