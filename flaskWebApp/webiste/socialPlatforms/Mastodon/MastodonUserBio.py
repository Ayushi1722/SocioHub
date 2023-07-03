import mastodon
from mastodon import Mastodon
from configparser import ConfigParser

from webiste.socialPlatforms.Mastodon.MastodonUserInfo import MastodonUserInfo


class MastodonUserBio:

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

    def get_userBio(self, user):
        keyList = ["FULLNAME", "SCREEN_NAME", "DESCRIPTION", "FOLLOWERS", "FOLLOWINGS"]
        dictionary = {}
        for i in keyList:
            dictionary[i] = None
        api = MastodonUserBio.get_api(self)
        users = api.account_search(user, limit=10, resolve=True)
        user_data = None
        for result in users:
            if result['username'] == user:
                user_data = result
                break

        if user_data:
            mastodonUser = MastodonUserInfo(user_data)
            dictionary['FULLNAME'] = mastodonUser.fullname
            dictionary['SCREEN_NAME'] = mastodonUser.screen_name
            dictionary['DESCRIPTION'] = mastodonUser.description
            dictionary['FOLLOWERS'] = mastodonUser.followers
            dictionary['FOLLOWINGS'] = mastodonUser.followings
        return dictionary
