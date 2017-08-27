# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-27 18:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grants', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='amount_offered',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='application',
            name='requested_ticket_only',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='application',
            name='special_reply_required',
            field=models.BooleanField(default=False),
        ),
    ]