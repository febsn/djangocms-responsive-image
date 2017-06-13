# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.template.loader import select_template
from django.utils.translation import ugettext_lazy as _
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from . import models
from .conf import settings
from .forms import ResponsiveImageForm

class ResponsiveImagePlugin(CMSPluginBase):
    module = 'Filer'
    model = models.ImagePlugin
    name = _('Responsive Image')
    form = ResponsiveImageForm
    TEMPLATE_NAME = 'djangocms_responsive_image/plugins/image/{0}.html'
    render_template = TEMPLATE_NAME.format('default')

    def render(self, context, instance, placeholder):
        style_name = instance.get_style_name()
        style = instance.get_style()
        self.render_template = select_template((
            self.TEMPLATE_NAME.format(style_name),
            self.TEMPLATE_NAME.format('default'))
        )
        # srcset list and srcset_2x dict are separated to support legacy templates
        srcset = []
        srcset_2x = {}
        for src in style['srcset']:
            if instance.image.width > src[0] and instance.image.height > src[1]:
                srcset.append(src)
                if settings.DJANGOCMS_RESPONSIVE_IMAGE_ADD_2X and instance.image.width >= src[0]*2 and instance.image.height >= src[1]*2:
                    srcset_2x[src[0]] = (src[0]*2, src[1]*2)
            else:
                srcset.append((instance.image.width, instance.image.height))
                break
        context.update({
            'srcset': srcset,
            'srcset_2x': srcset_2x,
            'sizes': style.get('sizes'),
            'default_size': style['default_size'],
            'style': style_name,
            'instance': instance,
            'placeholder': placeholder
        })
        return context

plugin_pool.register_plugin(ResponsiveImagePlugin)

