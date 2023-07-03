from configparser import ConfigParser
from instaloader import instaloader
from instaloader import TopSearchResults

from webiste.socialPlatforms.Instagram.InstagramUserInfo import InstagramUserInfo

class InstagramUserBio:

    def __init__(self, config_path):
        self.config_path = config_path

    def get_credentials(self):
        myconfig = ConfigParser()
        # myconfig.read('webiste/socialPlatforms/Instagram/config.ini')
        myconfig.read(self.config_path)
        username = myconfig['API']['USERNAME']
        password = myconfig['API']['PASSWORD']
        return username, password

    def get_userBio(self, user):
        keyList = ["FULLNAME", "USERNAME", "BIO", "FOLLOWERS", "FOLLOWING"]
        dictionary = {}
        for i in keyList:
            dictionary[i] = None
        L = instaloader.Instaloader()
        userName, passWord = InstagramUserBio.get_credentials(self)
        L.load_session_from_file(userName, "/Users/ayushi_nirmal/.config/instaloader/session-ayushi_sings")
        # L.context.log("Logging in...")
        # L.context.is_logged_in  # to check if you're already logged in
        # L.context.login(userName, passWord)
        profile = instaloader.Profile.from_username(L.context, user)
        instagramUser = InstagramUserInfo(profile)
        dictionary['FULLNAME'] = instagramUser.fullname
        dictionary['USERNAME'] = instagramUser.username
        dictionary['BIO'] = instagramUser.biography
        dictionary['FOLLOWERS'] = instagramUser.followers
        dictionary['FOLLOWING'] = instagramUser.followings
        return dictionary
