"""Image conversion classes and methods.

Methods for converting images as well as for creating a default image for use
upon image retrieval/conversion failures.
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from absl import logging
from PIL import Image
from PIL import ImageOps


DEFAULT_OPACITY = 0  # Between (0, 255)

# Conversion settings
_REQUIRED_MIN_DIMENSION = 10  # required minimum size of converted image


class ImageConvertSettings(object):
  """Image conversion settings."""
