import instaloader
from configparser import ConfigParser

def make_config():
    my_config_file = ConfigParser.read('config.ini')
    print(my_config_file)
    username = my_config_file['username']
    print(username)
    password = my_config_file['password']
    print(password)



if __name__ == '__main__':
    make_config()

#  # Get instance
# L = instaloader.Instaloader()
#
# # Login or load session
# L.login(username, password)
#
#
# # Obtain profile metadata
# profile = instaloader.Profile.from_username(L.context, "prada")
#
# # Print list of followees
#
#
#
# follow_list = []
# count=0
# for followee in profile.get_followers():
#     follow_list.append(followee.username)
#     file = open("prada_followers.txt","a+")
#     file.write(follow_list[count])
#     file.write("\n")
#     file.close()
#     print(follow_list[count])
#     count=count+1
# # (likewise with profile.get_followers())