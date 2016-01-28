# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_responsive_image', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageplugin',
            name='glossary',
            field=jsonfield.fields.JSONField(default={}),
        ),
    ]
