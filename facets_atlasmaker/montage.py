"""Utilities to combine converted images into atlas and to create manifest."""
import math
import os
from absl import logging
from PIL import Image


# Manifest Key names
MANIFEST_IMAGE_NAME_KEY = 'image_name'
MANIFEST_SOURCE_IMAGE_KEY = 'source_image'
MANIFEST_OFFSET_X_KEY = 'offset_x'
MANIFEST_OFFSET_Y_KEY = 'offset_y'
MANIFEST_IMAGE_FAIL_KEY = 'errors'


class SpriteAtlasSettings(object):
  """Sprite atlas settings."""

  def __init__(self, img_format, height=None, width=None,
               filename='spriteatlas', manifest_filename='manifest'):
    """

    Width and height are in units of number of images

    Args:
      img_format: output format (JPG, PNG, etc).
      height: Height of atlas in number of images.
      width: Width in number of images.
      filename: Desired filename of atlas (without file extension).
      manifest_filename: Desired filename of atlas manifest (without file
                         extension).
    """
    self._img_format = img_format
    self._width = width
    self._height = height
    self._filename = filename
    self._manifest_filename = manifest_filename

  
