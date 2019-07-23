"""Parallelize file fetch and conversion utilities and wrappers."""

from absl import logging
from joblib import Parallel, delayed
from PIL import ImageFile
import atlasmaker_io
import convert


def get_and_convert_image(image_location, image_convert_settings,
                          allow_truncated_images=False, disk_cache=False,
                          request_timeout=60, http_max_retries=2):
  
