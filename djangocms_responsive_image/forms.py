# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms

from .models import ImagePlugin
from .conf import settings

class GlossaryFormBase(forms.ModelForm):

    glossary_fields = tuple()

    def __init__(self, data=None, files=None, **kwargs):
        # set values for glossary form fields
        # values from initial overrule those from instance
        instance = kwargs.pop('instance', None)
        initial = kwargs.pop('initial', {})
        if instance and data is None:
            for field in self.glossary_fields:
                try:
                    initial[field] = initial.get(field, None) or instance.glossary[field]
                except KeyError:
                    pass
        return super(GlossaryFormBase, self).__init__(data=data, files=files, 
            instance=instance, initial=initial, **kwargs)

    def save(self, commit=True):
        if not commit:
            for field in self.glossary_fields:
                self.instance.glossary[field] = self.cleaned_data[field]
        return super(GlossaryFormBase, self).save(commit=commit)

class ResponsiveImageForm(GlossaryFormBase):
    STYLE_CHOICES = [
        (key, value['name'])
        for key, value
        in settings.DJANGOCMS_RESPONSIVE_IMAGE_IMAGE_STYLE_CHOICES.items()
    ]
    style = forms.ChoiceField(
        choices=STYLE_CHOICES)
    caption = forms.CharField(max_length=512, required=False)
    alt = forms.CharField(max_length=512, required=False)
    description = forms.CharField(widget=forms.Textarea, required=False)

    glossary_fields = ('style', 'caption', 'alt', 'description',)
    class Meta:
        model = ImagePlugin
        fields = ('image', )

