# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-19 21:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='pw_hash',
            field=models.CharField(default=0, max_length=60),
            preserve_default=False,
        ),
    ]