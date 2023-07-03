import time
import instaloader
from instaloader import Instaloader
from itertools import islice
import os
import pandas as pd
from configparser import ConfigParser

class InstagramData:

    def __init__(self, config_path):
        self.config_path = config_path

    def get_credentials(self):
        myconfig = ConfigParser()
        # myconfig.read('webiste/socialPlatforms/Instagram/config.ini')
        myconfig.read(self.config_path)
        username = myconfig['API']['USERNAME']
        password = myconfig['API']['PASSWORD']
        return username, password

    def get_followers(self, screen_name,  num):
        print("hello")
        username, password = InstagramData.get_credentials(self)
        print(username)
        L = instaloader.Instaloader()
        # L.login(username, password)
        L.load_session_from_file(username, "/Users/ayushi_nirmal/.config/instaloader/session-ayushi_sings")
        profile = instaloader.Profile.from_username(L.context, screen_name)
        # number_of_followers = num
        follower_list = []
        # print(str(profile.get_followers()))
        # followers = profile.get_followers()
        followers = set(islice(profile.get_followers(), int(num)))

        print(followers)
        for follower in followers:
            follower_list.append(follower.username)
        # InstagramData.save_data(screen_name, followers)
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

    # if __name__ == '__main__':
    #     username, password = get_credentials()
    #     target = 'cdcgov'
    #     L = instaloader.Instaloader()
    #     L.login(username, password)
    #     profile = instaloader.Profile.from_username(L.context, target)
    #     # profile = get_profile(username, password, target)
    #     number_of_followers = 1000
    #     followers = get_followers(profile, number_of_followers)
    #     for follower in followers:
    #         print(follower)
    #     print(len(followers))