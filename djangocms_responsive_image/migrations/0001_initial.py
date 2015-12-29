# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.image
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0002_auto_20150606_2003'),
        ('cms', '0013_urlconfrevision'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagePlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(to='cms.CMSPlugin', parent_link=True, primary_key=True, auto_created=True, serialize=False)),
                ('glossary', jsonfield.fields.JSONField()),
                ('image', filer.fields.image.FilerImageField(null=True, blank=True, to='filer.Image', verbose_name='image', default=None)),
            ],
            options={
                'verbose_name_plural': 'responsive filer images',
                'verbose_name': 'responsive filer image',
            },
            bases=('cms.cmsplugin',),
        ),
    ]
