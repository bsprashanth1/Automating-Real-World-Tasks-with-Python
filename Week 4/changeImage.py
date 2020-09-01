#!/usr/bin/env python3
import os
from PIL import Image

output_path = "supplier-data/images"


def scale_convert_image(path):
    for file in os.listdir(path):
        if ".tiff" in file:
            img = Image.open(path + "/" + file)
            new_img = img.convert("RGB")
            new_img = new_img.resize((600, 400))
            new_img.save(output_path + "/" + file.split('.')[0] + ".jpeg")


if __name__ == '__main__':
    scale_convert_image("supplier-data/images")
