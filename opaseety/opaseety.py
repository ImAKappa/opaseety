"""opaseety.py

Lorem Picsum: https://picsum.photos/
    Request specific size: https://picsum.photos/600
    Request specific image: https://picsum.photos/id/21/600 
Blending images: https://www.codespeedy.com/python-pil-image-blend-method/
"""

import argparse

import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from pathlib import Path

def blend(list_images):
    """Blend images 'equally' - according to the number of images
    
    TODO: A more 'equal' way of blending might take into account the color profiles and 2D features of the images
    Or maybe that wouldn't make a difference? Or make too much of a difference and make certain blends highly unbalanced?

    Creating a 'fair' blend is hard imo unless you take care to pick good input images.
    """
    equal_fraction = 1.0 / (len(list_images))
    output = np.zeros_like(list_images[0])
    for img in list_images:
        output = output + img * equal_fraction
    output = output.astype(np.uint8)
    return output

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Opaseety")
    parser.add_argument("--imagesets", "-i", required=True, type=Path, help="Directory containing sets of images to blend")
    # TODO:
    # parser.add_argument("--resize", "r", type=int, help="Dimension to resize")
    
    args = parser.parse_args()

    dim = (600, 600)

    imagesets_dir: Path = args.imagesets

    for img_dir in imagesets_dir.iterdir():
        print(f"Blending {img_dir.name}")
        # Convert each image to Image object
        images = [mpimg.imread(img_path) for img_path in img_dir.iterdir()]
        print("\tCollected images")
        resized_images = [cv2.resize(img, dim) for img in images]
        print("\tResized")
        # Blend images
        final_img = blend(images)
        final_name = imagesets_dir/f"./{img_dir.name}-final-blend.jpg"
        print(f"\tCompleted blending for {final_name}")
        plt.imsave(final_name, final_img)
        print("\tSaved")
