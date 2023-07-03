import os
import sys
import json
import time
import math
from tweepy import Cursor
import tweepy
import datetime as dt
import pandas as pd
from configparser import ConfigParser

class TwitterUsers():

    def __init__(self, config_path):
        self.config_path = config_path

    def get_api(self):
        myconfig = ConfigParser()
        # myconfig.read('webiste/socialPlatforms/Twitter/config.ini')
        myconfig.read(self.config_path)
        api_key = myconfig['API']['API_KEY']
        api_key_secret = myconfig['API']['API_KEY_SECRET']
        access_token = myconfig['API']['ACCESS_TOKEN']
        access_token_secret = myconfig['API']['ACCESS_TOKEN_SECRET']
        auth = tweepy.OAuth1UserHandler(api_key, api_key_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth, wait_on_rate_limit=True)
        return api

    def get_users(self,targetName):
        users = []
        api = TwitterUsers.get_api(self)
        profiles = api.search_users(targetName)
        # print the users retrieved
        for profile in profiles:
            users.append(profile.screen_name)
        return users[:3]

