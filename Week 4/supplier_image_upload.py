#!/usr/bin/env python3
import requests
import os

url = "http://localhost/upload/"

def upload_img(path):
    for file in os.listdir(path):
        if ".jpeg" in file:
            with open(path + "/" + file, 'rb') as opened:
                r = requests.post(url, files={'file': opened})

if __name__ == '__main__':
    upload_img("supplier-data/images")