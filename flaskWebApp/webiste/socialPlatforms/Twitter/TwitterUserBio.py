from configparser import ConfigParser
import tweepy
from webiste.socialPlatforms.Twitter.TwitterUserInfo import TwitterUserInfo

class TwitterUserBio:

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

    def get_userBio(self, user):
        keyList = ["FULLNAME", "SCREEN_NAME", "DESCRIPTION", "FOLLOWERS", "FOLLOWINGS", "LOCATION"]
        dictionary = {}
        for i in keyList:
            dictionary[i] = None
        api = TwitterUserBio.get_api(self)
        userInfo = api.get_user(screen_name=user)
        twitterUser = TwitterUserInfo(userInfo)
        dictionary['FULLNAME'] = twitterUser.fullname
        dictionary['SCREEN_NAME'] = twitterUser.screen_name
        dictionary['DESCRIPTION'] = twitterUser.description
        dictionary['FOLLOWERS'] = twitterUser.followers
        dictionary['FOLLOWINGS'] = twitterUser.followings
        dictionary['LOCATION'] = twitterUser.location
        return dictionary
