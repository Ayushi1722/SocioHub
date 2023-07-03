import json

from flask import Flask, jsonify, request

from webiste.socialPlatforms.Facebook.FacebookCall import FacebookCall
from webiste.socialPlatforms.Instagram.InstagramCall import InstagramCall
from webiste.socialPlatforms.Instagram.InstagramUserBio import InstagramUserBio
from webiste.socialPlatforms.Instagram.InstagramUsers import InstagramUsers
from webiste.socialPlatforms.Mastodon.MastodonUserBio import MastodonUserBio
from webiste.socialPlatforms.Mastodon.MastodonUsers import MastodonUsers
from webiste.socialPlatforms.Twitter.TwitterCall import TwitterCall
from webiste.socialPlatforms.Twitter.TwitterUserBio import TwitterUserBio
from webiste.socialPlatforms.Twitter.TwitterUsers import TwitterUsers
from flask import Flask
# import pymongo
from flask import Flask, render_template, request
from flask_pymongo import PyMongo
from pymongo import MongoClient

app = Flask(__name__)

MONGODB_URI = "mongodb+srv://anirmal_admin:Databases123@cluster0.5oiydpy.mongodb.net/"

# Connect to your MongoDB cluster:
client = MongoClient(MONGODB_URI)

# Define an endpoint for the root URL
@app.route('/')
def hello_world():
    return 'Hello, World!'

# @app.route('/add_user', methods=['POST'])
# def add_user():
#     name = request.form['name']
#     email = request.form['email']
#     mongo.db.users.insert_one({'name': name, 'email': email})
#     return redirect(url_for('index'))

# @app.route('/get_users/twitter', methods=['POST'])
@app.route('/get_users/twitter')
def get_twitter_users():
    target_name = request.args.get('target_name')
    twitterUsers = TwitterUsers(config_path='webiste/socialPlatforms/Twitter/config.ini')
    top3users = twitterUsers.get_users(target_name)

    # Access a specific database
    db = client["Users"]
    # Access a specific collection
    collection = db["Platforms"]

    # Create a document to insert
    document = {
        "platform": 'twitter',
        "query": target_name,
        "users": top3users
    }
    result = collection.insert_one(document)
    print("Inserted document ID:", result.inserted_id)
    # mongo.db.users.insert(dict(Platform='Twitter', Users=top3users))
    return top3users
    # return jsonify(top3users)

@app.route('/get_users/instagram')
def get_instagram_users():
    target_name = request.args.get('target_name')
    instagramUsers = InstagramUsers(config_path='webiste/socialPlatforms/Instagram/config.ini')
    top3users = instagramUsers.get_users(target_name)

    # Access a specific database
    db = client["Users"]
    # Access a specific collection
    collection = db["Platforms"]

    # Create a document to insert
    document = {
        "platform": 'instagram',
        "query": target_name,
        "users": top3users
    }
    result = collection.insert_one(document)
    print("Inserted document ID:", result.inserted_id)
    return top3users
    # return jsonify(top3users)

@app.route('/get_users/mastodon')
def get_mastodon_users():
    target_name = request.args.get('target_name')
    mastodonUsers = MastodonUsers(config_path='webiste/socialPlatforms/Mastodon/config.ini')
    top3users = mastodonUsers.get_users(target_name)

    # Access a specific database
    db = client["Users"]
    # Access a specific collection
    collection = db["Platforms"]

    # Create a document to insert
    document = {
        "platform": 'mastodon',
        "query": target_name,
        "users": top3users
    }
    result = collection.insert_one(document)
    print("Inserted document ID:", result.inserted_id)
    return top3users

# @app.route('/get_users/facebook')
# def get_facebook_users():
#     return 'facebook'

@app.route('/get_data/twitter')
def get_twitter_data():
    screen_name = request.args.get('name')
    max_followers= request.args.get('max_followers')
    twitterCallObj = TwitterCall()
    Followers_Twitter = twitterCallObj.get_twitter_data(str(screen_name), max_followers)
    return jsonify(Followers_Twitter)

@app.route('/get_data/instagram')
def get_instagram_data():
    screen_name = request.args.get('name')
    max_followers = request.args.get('max_followers')
    instaCallObj = InstagramCall()
    Followers_Instagram = instaCallObj.get_instagram_data(str(screen_name), max_followers)
    return jsonify(Followers_Instagram)

@app.route('/get_data/facebook')
def get_facebook_data():
    screen_name = request.args.get('name')
    max_followers = request.args.get('max_followers')
    facebookCallObj = FacebookCall()

@app.route('/get_bio/instagram')
def get_instagram_userBio():
    user = request.args.get('user')
    instagramUserBio = InstagramUserBio(config_path='webiste/socialPlatforms/Instagram/config.ini')
    instagramUserInfo = instagramUserBio.get_userBio(user)

    instagramUserInfo_JSON = json.dumps(instagramUserInfo)
    # Access a specific database
    db = client["User_description"]
    # Access a specific collection
    collection = db["Platforms_description"]


    # Create a document to insert
    document = {
        "platform": 'instagram',
        "query": user,
        "users": instagramUserInfo_JSON
    }
    result = collection.insert_one(document)
    print("Inserted document ID:", result.inserted_id)
    return instagramUserInfo

@app.route('/get_bio/twitter')
def get_twitter_userBio():
    user = request.args.get('user')
    twitterUserBio = TwitterUserBio(config_path='webiste/socialPlatforms/Twitter/config.ini')
    twitterUserInfo = twitterUserBio.get_userBio(user)

    twitterUserInfo_JSON = json.dumps(twitterUserInfo)
    # Access a specific database
    db = client["User_description"]
    # Access a specific collection
    collection = db["Platforms_description"]

    # Create a document to insert
    document = {
        "platform": 'twitter',
        "query": user,
        "users": twitterUserInfo_JSON
    }
    result = collection.insert_one(document)
    print("Inserted document ID:", result.inserted_id)

    return twitterUserInfo

@app.route('/get_bio/mastodon')
def get_mastodon_userBio():
    user = request.args.get('user')
    mastodonUserBio = MastodonUserBio(config_path='webiste/socialPlatforms/Mastodon/config.ini')
    mastodonUserInfo = mastodonUserBio.get_userBio(user)

    mastodonUserInfo_JSON = json.dumps(mastodonUserInfo)
    # Access a specific database
    db = client["User_description"]
    # Access a specific collection
    collection = db["Platforms_description"]

    # Create a document to insert
    document = {
        "platform": 'mastodon',
        "query": user,
        "users": mastodonUserInfo_JSON
    }
    result = collection.insert_one(document)
    print("Inserted document ID:", result.inserted_id)

    return mastodonUserInfo

if __name__ == '__main__':
    # user = get_twitter_userBio()
    # print(user)
    app.debug = True
    app.run()






