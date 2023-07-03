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

def get_api():
    api_key = 'dKWN9rkILE25I2Dk4a8sTLJ9S'
    api_key_secret = '9z4cCWoHGHfcxPeK060ncrekb5T9h8fsUr2NLlvBpPeJhelKfd'
    access_token = '1570146620653850629-avBFXimmebUI4wXrQA7RaYlf8TXasr'
    access_token_secret = '8V4Y1i2hPSur1UmCyrLB1aUNI3xgRSWLjUbezHrmiuL7R'
    auth = tweepy.OAuth1UserHandler(api_key, api_key_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    return api

def save_data(screen_name, data):
    if not os.path.isdir("/Users/ayushi_nirmal/PycharmProjects/junk/users/{}".format(screen_name)):
        os.makedirs("/Users/ayushi_nirmal/PycharmProjects/junk/users/{}".format(screen_name))
    fname = "/Users/ayushi_nirmal/PycharmProjects/junk/users/{}/".format(screen_name) + "followers"
    # df_data = {'names': data};
    # print(df_data);
    df = pd.DataFrame(data)
    # print(df)
    df.to_csv(fname + ".csv", index=False)

def get_followers(api, screen_name):
    max_followers = 5000
    followers = []
    while(len(followers) < max_followers):
        try:
            for page in Cursor(api.get_followers, screen_name= screen_name, count=200).pages(50):
                # print(page)
                for follower in page:
                    # print(page)
                    name = f"{follower.id} - {follower.name} - {follower.screen_name}"
                    followers.append(name)
                print(len(page))
            print(f"Followers: {len(followers)}")
        except tweepy.errors.TweepyException:
            print('Exception raised, waiting for 15 minutes')
            print('(until:', dt.datetime.now() + dt.timedelta(minutes=15), ')')
            time.sleep(15 * 60)
    save_data(screen_name, followers)
    return followers

if __name__ == '__main__':
    api = get_api()
    # screen_name = 'narendramodi'
    # screen_name = 'elonmusk'
    # screen_name = 'realDonaldTrump'
    screen_name = 'JoeBiden'
    followers = get_followers(api, screen_name)
    print(len(followers))


