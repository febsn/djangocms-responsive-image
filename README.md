djangocms-responsive-image
==========================

This package provides a plugin for Django CMS 3 similar to
cmsplugin\_filer\_image, but in addition can deliver multiple sizes as a html5
srcset attribute for the img tag.

configuration
-------------

How the srcset is built is determined by the style choices attribute.
You can configure them via the `DJANGOCMS_RESPONSIVE_IMAGE_IMAGE_STYLE_CHOICES`
setting:

    DJANGOCMS_RESPONSIVE_IMAGE_IMAGE_STYLE_CHOICES = {
        'fullwidth': {
            'name': _('full width'),
            'srcset': ((960, 0), (640, 0), ),
            'sizes': '(max-width: 800px) 640px',
            'default_size': (960, 0)
        }
    }

`srcset` ist a tuple of (width, height) tuples which will be used to create 
the `srcset` img attribute and also to render the thumbnails with 
`easy_thumbnails`.
`sizes` is the value of the `sizes` img attribute, refer to your favorite html5
documentation for information on how to use it. You can also omit it if
unnecessary.
`default_size` will be used for the `src` attribute and the corresponding thumbnail as a fallback for browsers which don't support `srcset`.

