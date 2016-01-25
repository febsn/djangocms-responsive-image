# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from appconf import AppConf

class ResponsiveImageAppConf(AppConf):
    IMAGE_STYLE_CHOICES = {
        'default': {
            'name': _('default'),
            'srcset': ((300, 0), (800, 0), (1600, 0), (2000, 0)),
            'sizes': None,
            'default_size': (1600, 0),
        },
    }
    IMAGE_DEFAULT_STYLE = 'default'

