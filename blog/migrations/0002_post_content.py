# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=django_markdown.models.MarkdownField(default=datetime.datetime(2015, 4, 10, 16, 19, 37, 697459)),
            preserve_default=False,
        ),
    ]
