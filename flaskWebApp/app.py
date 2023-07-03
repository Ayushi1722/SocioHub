from flask import Flask, jsonify, request

from webiste.socialPlatforms.Instagram.InstagramCall import InstagramCall
from webiste.socialPlatforms.Twitter.TwitterCall import TwitterCall

app = Flask(__name__)

# Define an endpoint for the root URL
@app.route('/')
def hello_world():
    return 'Hello, World!'

# # Define an endpoint for returning JSON data
# @app.route('/api/data')
# def get_data():
#     data = {'name': 'John Doe', 'age': 30, 'city': 'New York'}
#     return jsonify(data)

# @app.route('/api/get_data')
# def get_data(screen_name, platform):
#     url = f"https:/127.0.0.1/api/get_data'param1={screen_name}&param2={platform}"
#     response = request.get(url)
#     if response.status_code == 200:
#         return response.json()
#     else:
#         return None

# Define an endpoint for accepting POST requests
# @app.route('/api/add_data', methods=['POST'])
# def add_data():
#     data = request.get_json()
#     name = request.args.get('name')
#
#     # do something with the data, e.g. add it to a database
#     return 'Data added successfully'

# @app.route('/api/get_data/twitter', method=['POST'])
# def get_twitter_data():
#     screen_name = request.args.get('name')
#     max_followers= request.args.get('max_followers')
#     twitterCallObj = TwitterCall()
#     Followers_Twitter = twitterCallObj.get_instagram_data(screen_name, max_followers)
#     return Followers_Twitter

@app.route('/get_data/instagram')
def get_instagram_data():
    screen_name = request.args.get('name')
    max_followers = request.args.get('max_followers')
    instaCallObj = InstagramCall()
    Followers_Instagram = instaCallObj.get_instagram_data(screen_name, max_followers)
    return Followers_Instagram


if __name__ == '__main__':
    app.run()



