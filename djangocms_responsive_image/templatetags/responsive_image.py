# -*- coding: utf-8 -*-

from django import template

from ..conf import settings
from ..utils import create_srcset

register = template.Library()

@register.inclusion_tag("djangocms_responsive_image/snippets/image.html")
def responsive_image(image, style_name=None, widths=None, sizes=None, default_size=None, aspect_ratio=0, alt='', classes=''):
    if widths:
        widths = [int(w) for w in widths.split(',')]
    else:
        if not style_name:
            style_name = settings.DJANGOCMS_RESPONSIVE_IMAGE_IMAGE_DEFAULT_STYLE
        style = settings.DJANGOCMS_RESPONSIVE_IMAGE_IMAGE_STYLE_CHOICES[style_name]
        widths = style.get('widths')
        aspect_ratio = style.get('aspect_ratio')
        default_size = style.get('default_size')
    srcset = create_srcset(image, widths, aspect_ratio, settings.DJANGOCMS_RESPONSIVE_IMAGE_ADD_2X)
    if not default_size:
        default_size = (widths[0], widths[0]*aspect_ratio)
    context = {
        'alt': alt,
        'image': image,
        'srcset': srcset,
        'sizes': sizes,
        'default_size': default_size,
        'style': style_name,
        'classes': '',
    }
    return context
