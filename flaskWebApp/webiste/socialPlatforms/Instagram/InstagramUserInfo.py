from configparser import ConfigParser
from instaloader import instaloader
from instaloader import TopSearchResults
from enum import Enum

class InstagramUserInfo():

    def __init__(self, profile):
        self.fullname = profile.full_name
        self.username = profile.username
        self.biography = profile.biography
        self.followers = profile.followers
        self.followings = profile.followees
