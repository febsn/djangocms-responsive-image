# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.exceptions import ImproperlyConfigured
from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models import CMSPlugin
from filer.fields.image import FilerImageField
from jsonfield.fields import JSONField

from .conf import settings

class ImagePluginBase(CMSPlugin):
    glossary = JSONField(default={})

    class Meta:
        abstract = True

class ImagePlugin(ImagePluginBase):
    image = FilerImageField(null=True, blank=True, default=None, verbose_name=_("image"))

    class Meta:
        verbose_name = _('responsive filer image')
        verbose_name_plural = _('responsive filer images')

    def get_style_name(self):
        return self.glossary.get('style',
            settings.DJANGOCMS_RESPONSIVE_IMAGE_IMAGE_DEFAULT_STYLE)

    def get_style(self):
        try:
            return settings.DJANGOCMS_RESPONSIVE_IMAGE_IMAGE_STYLE_CHOICES[
                self.get_style_name()]
        except KeyError:
            error_msg = ("ResponsiveImage style {0} is used by plugin {1}, "
                         "but not defined in the settings.").format(
                            self.get_style_name(), self)
            raise ImproperlyConfigured(error_msg)

    def alt(self):
        return self.glossary.get('alt', None) or self.image.default_alt_text or ''

    def __str__(self):
        return self.image.label

