#!/usr/bin/python
# Author: Nam Nguyen Hoai
# This file is to get content from a website

import os
import time
import datetime
from bs4 import BeautifulSoup
from requests_futures.sessions import FuturesSession

URL = "http://113.190.232.90:3333/"
PATH_STORE = "/root-tmp"
FILE_NAME = PATH_STORE + "/web.txt"
SIZE = 512000
session = FuturesSession()


def get_content():
    content = session.get(URL)
    return content.result()


def convert_html_to_text(content_html):
    content_text = BeautifulSoup(content_html, 'html.parser')
    return content_text.get_text()


def create_file(url_file, content_file):
    if os.path.exists(url_file):
        if os.path.getsize(url_file) > SIZE:
            now = datetime.datetime.now().strftime("%H_%M_%Y_%m_%d")
            new_name_file = url_file + '_' + now
            os.rename(url_file, new_name_file)
            with open(url_file, 'a') as f:
                f.write(content_file)
        else:
            with open(url_file, 'a') as f:
                f.write(content_file)
    else:
        with open(url_file, 'a') as f:
            f.write(content_file)


if __name__ == "__main__":
    if not os.path.exists(PATH_STORE):
        os.makedirs(PATH_STORE, mode=0755)
    while True:
        time.sleep(30)
        content_web = get_content().content
        content_text = convert_html_to_text(content_web)
        create_file(FILE_NAME, content_text)
