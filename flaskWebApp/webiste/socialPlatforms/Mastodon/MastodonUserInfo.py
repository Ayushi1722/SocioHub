class MastodonUserInfo():

    def __init__(self, user):
        self.fullname = user.display_name
        self.screen_name = user.username
        self.description = user.note
        self.followers = user.followers_count
        self.followings = user.following_count