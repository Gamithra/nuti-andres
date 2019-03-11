#!/usr/bin/python3
# -*- coding:utf-8 -*-

import markovify, config

def fillQueue():
    with open(config.project_path+"tode-queue.txt", "r+b") as queue:
        with open(config.project_path+"/data/todejaoigus.txt") as f:
            text = f.read()
        text_model = markovify.Text(text)
        content = queue.read().decode('UTF-8')
        for i in range(15):
            queue.write(bytes(text_model.make_short_sentence(170), 'UTF-8'))
            queue.write(bytes("\n", 'UTF-8'))

fillQueue()
