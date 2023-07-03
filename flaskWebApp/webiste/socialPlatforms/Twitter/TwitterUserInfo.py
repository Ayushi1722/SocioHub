from configparser import ConfigParser
from instaloader import instaloader
from instaloader import TopSearchResults
from enum import Enum

class TwitterUserInfo():

    def __init__(self, user):
        self.fullname = user.name
        self.screen_name = user.screen_name
        self.description = user.description
        self.followers = user.followers_count
        self.followings = user.friends_count
        self.location = user.location
