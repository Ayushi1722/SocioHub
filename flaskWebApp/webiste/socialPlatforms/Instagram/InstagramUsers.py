from configparser import ConfigParser
from instaloader import instaloader
from instaloader import TopSearchResults

class InstagramUsers:

    def __init__(self, config_path):
        self.config_path = config_path

    def get_credentials(self):
        myconfig = ConfigParser()
        # myconfig.read('webiste/socialPlatforms/Instagram/config.ini')
        myconfig.read(self.config_path)
        username = myconfig['API']['USERNAME']
        password = myconfig['API']['PASSWORD']
        return username, password

    def get_users(self, targetName):
        users = []
        L = instaloader.Instaloader()
        userName, passWord = InstagramUsers.get_credentials(self)
        # L.login(username, password)
        L.load_session_from_file(userName, "/Users/ayushi_nirmal/.config/instaloader/session-ayushi_sings")
        # L.context.log("Logging in...")
        # L.context.is_logged_in  # to check if you're already logged in
        # L.context.login(userName, passWord)
        top_search_results = TopSearchResults(L.context, targetName)
        profiles = top_search_results.get_profiles()
        for profile in profiles:
            users.append(profile.username)
            # print(profile.full_name)
            # print(profile.username)
        return users[:3]
