"""blend.py

Module for blending images together
"""
from .utils import all_equal
from pathlib import Path
import numpy as np
import matplotlib.image as mpimg
from typing import Optional
import cv2

class ImageBlend:
    """A blend of images"""

    def __init__(self, image_matrices: list[np.ndarray]):
        self.images = image_matrices
        self.n_images = len(image_matrices)
        self.__validate()

    @classmethod
    def load_images(cls, img_dir: Path, resize: Optional[int]=None):
        """Assumes square images, which is why `resize` is only an int"""
        images_matrices = [mpimg.imread(img_path) for img_path in img_dir.iterdir()]
        if resize:
            images_matrices = [cv2.resize(img, (resize, resize)) for img in images_matrices]
        return cls(images_matrices)

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