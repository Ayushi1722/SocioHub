import time
import instaloader
from instaloader import Instaloader
from itertools import islice
import os
import pandas as pd
L = instaloader.InstaLoader()

def get_profile(username, password, target):
    L.login(username, password)
    profile = instaloader.Profile.from_username(L.context, target)
    return profile

def get_followers(profile, num):
    follower_list = []
    followers = set(islice(profile.get_followers(), num))
    for follower in followers:
        # print(follower.username)
        # print(len(follower_list))
        follower_list.append(follower.username)
    # print(len(follower_list))
    save_data(profile.full_name, follower_list)
    return follower_list

def save_data(screen_name, data):
    if not os.path.isdir("/Users/ayushi_nirmal/PycharmProjects/junk/users_instagram/{}".format(screen_name)):
        os.makedirs("/Users/ayushi_nirmal/PycharmProjects/junk/users_instagram/{}".format(screen_name))
    fname = "/Users/ayushi_nirmal/PycharmProjects/junk/users_instagram/{}/".format(screen_name) + "followers"
    # df_data = {'names': data};
    # print(df_data);
    df = pd.DataFrame(data)
    # print(df)
    df.to_csv(fname + ".csv", index=False)

if __name__ == '__main__':
    username = 'ayushi_sings'
    password = 'Crazy@17'
    target = 'cdcgov'
    profile = get_profile(username, password, target)
    number_of_followers = 1000
    followers = get_followers(profile, number_of_followers)
    for follower in followers:
        print(follower)
    print(len(followers))
