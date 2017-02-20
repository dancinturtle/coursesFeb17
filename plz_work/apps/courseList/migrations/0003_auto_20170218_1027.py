# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-18 18:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courseList', '0002_auto_20170217_1725'),
    ]

    operations = [
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='course',
            name='description',
        ),
        migrations.AddField(
            model_name='description',
            name='course_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='courseList.Course'),
        ),
    ]
