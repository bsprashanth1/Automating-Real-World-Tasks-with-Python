#! /usr/bin/env python3

import os
import requests
import json


def make_requests(path):

    for file in os.listdir(path):
        data = {}
        with open(path + "/" +file, 'r', encoding='utf-8') as text:
            test_list = text.readlines()
            data["name"] = test_list[0].replace("\n","")
            data["weight"] = int(test_list[1].split(' ')[0])
            data["description"] = test_list[2].replace("\n","")
            data["image_name"] = file.replace("txt","jpeg")
        response = requests.post("http://34.121.112.106/fruits/", json=data)
        print(response.status_code)
        print(response.request.body)


if __name__ == '__main__':
    make_requests("supplier-data/descriptions")
