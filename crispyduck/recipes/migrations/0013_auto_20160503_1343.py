# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-03 13:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0012_recipeinstruction_ingredient'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='recipeinstruction',
            name='quantity',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=3),
        ),
        migrations.AlterField(
            model_name='recipeinstruction',
            name='ingredient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.Ingredient'),
        ),
        migrations.AddField(
            model_name='recipeinstruction',
            name='unit',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='recipes.Unit'),
        ),
    ]