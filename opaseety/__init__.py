# SPDX-FileCopyrightText: 2024-present ImAKappa <imaninconsp1cuouskappa@gmail.com>
#
# SPDX-License-Identifier: MIT

import argparse

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from pathlib import Path

from opaseety.blend import ImageBlend
from nicegui import ui

def main() -> None:
    print("OPASEETY (v0.1.0)\n")
    parser = argparse.ArgumentParser("Opaseety")
    parser.add_argument("--imagesets", "-i", required=True, type=Path, help="Directory containing sets of images to blend")
    parser.add_argument("--resize", "-r", type=int, default=None, help="Dimension to resize [not implemented yet]")
    args = parser.parse_args()

    imagesets_dir: Path = args.imagesets

    for img_dir in imagesets_dir.iterdir():
        if img_dir.is_file():
            continue

        print(f"Blending {img_dir.name} ... ", end="")

        imgblend = ImageBlend.load_images(img_dir, args.resize)
        blended_image = imgblend.equal_opacity()
        print("DONE")
        
        output_file = imagesets_dir/f"{img_dir.name}-final-blend.jpg"
        plt.imsave(output_file, blended_image)
        print(f"Saved to '{output_file}'")
        print()