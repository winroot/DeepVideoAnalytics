# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-16 07:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dvaui', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExternalServer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=300, unique=True)),
                ('url', models.CharField(default='', max_length=1000, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='externalserver',
            unique_together=set([('name', 'url')]),
        ),
    ]