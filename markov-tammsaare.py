#!/usr/bin/python3
# -*- coding:utf-8 -*-
import markovify, tweepy
from random import randint
import config

tweet_content = ""
hashtags = ["tõdejaõigus", "tammsaare", "vargamäerobot", "nutiandres"]

queue = open(config.project_path+"tode-queue.txt", "r+b")
queue_line = queue.readline().decode('UTF-8')

if queue_line != "":
    tweet_content = queue_line.strip()
    left = queue.read().decode('UTF-8')
    queue.close()
    queue = open(config.project_path+"tode-queue.txt", "w")
    queue.write(left)

else:
    with open(config.project_path+"/data/todejaoigus.txt") as f:
        text = f.read()
    text_model = markovify.Text(text)
    tweet_content = text_model.make_short_sentence(170)

auth = tweepy.OAuthHandler(config.consumer_token, config.consumer_secret)
auth.set_access_token(config.token_key, config.token_secret)
api = tweepy.API(auth)

random_tag = hashtags[randint(0, len(hashtags)-1)]
tweet = tweet_content + " #" + random_tag
print(tweet)

api.update_status(tweet)
