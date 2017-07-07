# -*- coding: utf-8 -*-

from __future__ import division

def create_srcset(image, widths, aspect_ratio=0, add_2x=True):
    # We take the reciprocal value of the aspect ratio as a factor on the height
    try:
        ratio_reciprocal = 1 / aspect_ratio
    except ZeroDivisionError:
        # Set the factor to 0, hence no height constraint
        ratio_reciprocal = 0

    srcset = []
    for width in widths:
        height = width * ratio_reciprocal
        if image.width > width and image.height > height:
            srcset.append((width, height))
            if add_2x and image.width >= width*2 and image.height >= height*2:
                srcset.append((width*2, height*2))
        else:
            srcset.append((image.width, image.width*ratio_reciprocal))
            break
    return srcset
