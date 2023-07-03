#from webiste.socialPlatforms.Twitter import TwitterData
from webiste.socialPlatforms.Twitter.TwitterData import TwitterData

class TwitterCall():
    # def get_twitter_data(self, screen_name, max_followers):
    def get_twitter_data(self, screen_name, max_followers):
        print('twitterCall')
        twitterDataObj = TwitterData(config_path='webiste/socialPlatforms/Twitter/config.ini')
        api = twitterDataObj.get_api()
        print("API")
        print(api)
        # max_followers = 5000
        followers = twitterDataObj.get_followers(api, screen_name, int(max_followers))
        print(followers)
        return followers