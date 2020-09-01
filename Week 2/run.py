#! /usr/bin/env python3

import os
import requests
import json


def make_requests(path):

    for file in os.listdir(path):
        data = {}
        with open(path + "/" +file, 'r', encoding='utf-8') as text:
            test_list = text.readlines()
            data["title"] = test_list[0].replace("\n","")
            data["name"] = test_list[1].replace("\n","")
            data["date"] = test_list[2].replace("\n","")
            data["feedback"] = test_list[3].replace("\n","")
        response = requests.post("http://34.121.121.122/feedback/", json=data)
        print(response.status_code)
        print(response.request.body)

if __name__ == '__main__':
    input_data_path = "/data/feedback"
    make_requests(input_data_path)
