# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-09 17:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255, unique=True)),
                ('first_name', models.CharField(max_length=255)),
                ('middle_name', models.CharField(max_length=255, null=True)),
                ('last_name', models.CharField(max_length=255)),
                ('affiliation', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('abstract', models.TextField()),
                ('author_emails', models.TextField()),
                ('first_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bidding.Author')),
            ],
        ),
    ]