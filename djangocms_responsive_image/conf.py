# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings

from appconf import AppConf

class ResponsiveImageAppConf(AppConf):
    IMAGE_STYLE_CHOICES = {
        'default': {
            'srcset': ((300, 0), (800, 0), (1600, 0), (2000, 0)),
            'sizes': None,
            'default_size': (1600, 0),
        },
    }
    IMAGE_DEFAULT_STYLE = 'default'

