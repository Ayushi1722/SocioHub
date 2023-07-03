from webiste.socialPlatforms.Facebook.FacebookData import FacebookData

class FacebookCall():
    # def get_instagram_data(self, screen_name, max_followers):
    def get_facebook_data(self, screen_name, max_followers):
        print("insta call")
        facebookDataObj = FacebookData(config_path='webiste/socialPlatforms/Facebook/config.ini')
        followers = facebookDataObj.get_users(screen_name, int(max_followers))
        return followers