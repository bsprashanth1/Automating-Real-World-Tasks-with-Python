import os
from PIL import Image

output_path = "/opt/icons/"


def scale_convert_image(path):
    for file in os.listdir(path):
        img = Image.open(path + "/" + file)
        new_img = img.convert("RGB")
        new_img.rotate(90).resize((128, 128))
        new_img.save(output_path + "/" + file + ".jpg")


if __name__ == '__main__':
    input_path = os.getcwd() + "images/"
    scale_convert_image(input_path)
