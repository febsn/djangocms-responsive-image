djangocms-responsive-image
==========================

This package provides a plugin for Django CMS 3 similar to
cmsplugin\_filer\_image, but in addition can deliver multiple sizes as a html5
srcset attribute for the img tag.

# Configuration

How the srcset is built is determined by the style choices attribute.
You can configure them via the `DJANGOCMS_RESPONSIVE_IMAGE_IMAGE_STYLE_CHOICES`
setting:

    DJANGOCMS_RESPONSIVE_IMAGE_IMAGE_STYLE_CHOICES = {
        'fullwidth': {
            'name': _('full width'),
            'widths': (960, 640),
            'aspect_ratio': 16/9,
            'sizes': '(max-width: 800px) 640px',
            'default_width': 960,
        }
    }

`width` ist a list of width values which will be used to create 
the `srcset` img attribute and also to render the thumbnails with 
`easy_thumbnails`.

`aspect_ratio` will be used to calculate the height attribute for each 
source. Set it to `0` to use the source image's aspect ratio. Remember to
`from __future__ import unicode_literals` if you use Python 2.

`sizes` is the value of the `sizes` img attribute, refer to your favorite html5
documentation for information on how to use it. You can also omit it if
unnecessary.

`default_size` will be used for the `src` attribute and the corresponding thumbnail as a fallback for browsers which
don't support `srcset`.

By default, the srcset includes high-resolution (2x) images if the source image is large enough. You can disable
this behaviour by setting `DJANGOCMS_RESPONSIVE_IMAGE_ADD_2X = False`.

# Usage outside the CMS (template tag)

You can include responsive images also using the `responsive_image` template tag.
Add `{% load responsive_image %}` to your template to use it.

Please note that unlike the plugin, the template tag always uses the `djangocms-responsive-image/snippets/image.html` template,
even if a predefined style is used.

There are two options to specify the source sets:

## Using style choices
You can refer to the same style choices defined in your settings that the plugin uses, e.g.:

`{% responsive_image image "default" alt="Alt text" classes="img-responsive" %}`

## Specifying widths directly
You can specify the attributes directly without using a style choice, e.g.:

`{% responsive_image image widths="600,900,1200" aspect_ratio=3 alt="Alt text" %}

## Full list of arguments
* `image`: The Image instance to use
* `style_name`: The name of the style choice to use. Has precedence over `widths`, `default_width` and `aspect_ratio`.
* `widths`: A comma-separated list of widths to use, for example `600,1200`. Will be ignored if a style choice is defined.
* `default_width`: Width that will be used for the `src` fallback tag for browsers that don't support `srcset`. Will be ignored if a style choice is specified.
* `aspect_ratio`: Aspect ratio for cropping the images. Set to `0` to keep the image's original aspect ratio. Will be ignored if a style choice is specified.
* `sizes`: A string that will be set as the `img`'s `sizes` attribute. Refer to your favorite html5 documentation for more information.
* `alt`: Alt tag for the image.
* `classes`: CSS classes for the `img` tag.


# Changelog

- 0.2     changed conf syntax (`widths`, `aspect\_ratio` and `default\_width` instead of `srcset` attribute), added template tag
          that can be used outside the cms
- 0.1.1   added support for high-res images; bugfix
- 0.1.0   added description field and alt getter with fallback to the default\_alt\_text of the image
- 0.0.11  added fallback src attribute to default template
