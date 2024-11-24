"""blend.py

Module for blending images together
"""
from .utils import all_equal
import numpy as np

class ImageBlend:
    """A blend of images"""

    def __init__(self, images: list[np.ndarray]):
        self.images = images
        self.n_images = len(images)
        self.__validate()

    def __validate(self):
        """Validate images"""
        # Check that all images have the same dimension
        dims = [img.shape for img in self.images]
        if not all_equal(dims):
            raise ValueError("Images must all have the same dimension")

    def equal_opacity(self) -> None:
        """Blend images 'equally'"""
        equal_fraction = 1.0 / self.n_images
        output = np.zeros_like(self.images[0])
        for img in self.images:
            output = output + img * equal_fraction
        output = output.astype(np.uint8)
        return output