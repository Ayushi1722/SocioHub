#from webiste.socialPlatforms.Twitter import TwitterData
from webiste.socialPlatforms.Instagram.InstagramData import InstagramData

class InstagramCall():
    # def get_instagram_data(self, screen_name, max_followers):
    def get_instagram_data(self, screen_name, max_followers):
        print("insta call")
        instagramDataObj = InstagramData(config_path='webiste/socialPlatforms/Instagram/config.ini')
        # api = instagramDataObj.get_api()
        # max_followers = 5000
        followers = instagramDataObj.get_followers(screen_name, int(max_followers))
        # print(followers)
        return followers