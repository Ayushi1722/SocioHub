import csv
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


class TwitterData:

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

    def save_data(self, screen_name, data):
        if not os.path.isdir("/Users/ayushi_nirmal/PycharmProjects/junk/users/{}".format(screen_name)):
            os.makedirs("/Users/ayushi_nirmal/PycharmProjects/junk/users/{}".format(screen_name))
        fname = "/Users/ayushi_nirmal/PycharmProjects/junk/users/{}/".format(screen_name) + "followers"
        # df_data = {'names': data};
        # print(df_data);
        df = pd.DataFrame(data)
        # print(df)
        df.to_csv(fname + ".csv", index=False)

    def get_followers(self, api, screen_name, max_followers):
        followers = []
        # while (len(followers) < max_followers):
        try:
            for page in Cursor(api.get_followers, screen_name=screen_name, count=max_followers).pages(1):
                # print(page)
                for follower in page:
                    # print(page)
                    # name = f"{follower.id} - {follower.name} - {follower.screen_name}"
                    name = follower.screen_name
                    followers.append(name)
                print(len(page))
            print(f"Followers: {len(followers)}")
        except tweepy.errors.TweepyException:
            print('Exception raised, waiting for 15 minutes')
            print('(until:', dt.datetime.now() + dt.timedelta(minutes=15), ')')
            time.sleep(15 * 60)
        # TwitterData.save_data(screen_name, followers)
        return followers