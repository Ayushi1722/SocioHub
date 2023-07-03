import mastodon
from mastodon import Mastodon
from configparser import ConfigParser

class MastodonUsers():

    def __init__(self, config_path):
        self.config_path = config_path

    def get_api(self):
        myconfig = ConfigParser()
        # myconfig.read('webiste/socialPlatforms/Mastodon/config.ini')
        myconfig.read(self.config_path)
        # client_key = myconfig['API']['CLIENT_KEY']
        # client_secret = myconfig['API']['CLIENT_SECRET']
        access_token = myconfig['API']['ACCESS_TOKEN']
        base_url = myconfig['API']['BASE_URL']
        mastodon = Mastodon(access_token=access_token, api_base_url=base_url)
        return mastodon

    def get_users(self, targetName):
        api = MastodonUsers.get_api(self)
        users = api.account_search(targetName)
        # print the users retrieved
        users_list = []
        for user in users:
            # print(user['username'])
            users_list.append(user['username'])
        return users_list[:3]

