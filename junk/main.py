import tkinter as tk
from tkinter import *
from tkinter import *
from tkinter import Tk
from tkinter import *
import requests
# Create the Tkinter window
# window = tk.Tk()
window = Tk()
# width, height = window.winfo_screenmmwidth(), window.winfo_screenheight()
# window.geometry('%dx%d+0+0' % (width, height))

window.title("Social Media App")

# Get the screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Set the window size to match the screen size
window.geometry(f"{screen_width}x{screen_height}")

# http://127.0.0.1:5000/get_users/instagram?target_name=bohan
def get_users(platform, user):
    # Make a request to the Flask API
    response = requests.get(f'http://127.0.0.1:5000/get_users/{platform}?target_name={user}')
    result = response.text
    return result

def get_info(platform, user):
    # Make a request to the Flask API
    response = requests.get(f'http://127.0.0.1:5000/get_bio/{platform}?user={user}')
    result = response.text
    return result

def button_click_twitter(user):
    platform = 'twitter'
    data = get_info(platform, user)
    data = eval(data)
    textbox_twitterUsers.delete('1.0', tk.END)
    textbox_twitterUsers.insert(tk.END, data)

def button_click_instagram(user):
    platform = 'instagram'
    data = get_info(platform, user)
    data = eval(data)
    textbox_instagramUsers.delete('1.0', tk.END)
    textbox_instagramUsers.insert(tk.END, data)

def button_click_mastodon(user):
    platform = 'mastodon'
    data = get_info(platform, user)
    data = eval(data)
    textbox_mastodonUsers.delete('1.0', tk.END)
    textbox_mastodonUsers.insert(tk.END, data)

########################
def on_click_twitter():
    user = platform_twitter_user.get()
    results = get_users('twitter', user)
    results = eval(results)
    destroy_buttons(buttons_twitter)
    buttons_twitter.clear()
    i = 3
    buttons = []
    for result in results[:3]:
        button = tk.Button(window, text=result, command=lambda btn=result: button_click_twitter(btn))
        button.grid(row=i, column=0)
        buttons_twitter.append(button)
        i = i + 1

def on_click_instagram():
    user = platform_instagram_user.get()
    results = get_users('instagram', user)
    results = eval(results)
    destroy_buttons(buttons_instagram)
    buttons_instagram.clear()
    i = 3
    buttons = []
    for result in results[:3]:
        button = tk.Button(window, text=result, command=lambda btn=result: button_click_instagram(btn))
        button.grid(row=i, column=1)
        buttons_instagram.append(button)
        i = i + 1

def on_click_mastodon():
    user = platform_mastodon_user.get()
    results = get_users('mastodon', user)
    results = eval(results)
    destroy_buttons(buttons_mastodon)
    buttons_mastodon.clear()
    i = 3
    buttons = []
    for result in results[:3]:
        button = tk.Button(window, text=result, command=lambda btn=result: button_click_mastodon(btn))
        button.grid(row=i, column=2)
        buttons_mastodon.append(button)
        i = i + 1

def destroy_buttons(button_list):
    for button in button_list:
        button.destroy()

#Creating the input widgets for Twitter, Instagram, Facebook
#Twitter
platform_twitter = tk.Label(window, text="Twitter User Search")
platform_twitter.grid(row=0, column=0)
platform_twitter_user = tk.Entry(window)
platform_twitter_user.grid(row=1, column=0)

#Instagram
platform_instagram = tk.Label(window, text="Instagram User Search")
platform_instagram.grid(row=0, column=1)
platform_instagram_user = tk.Entry(window)
platform_instagram_user.grid(row=1, column=1)

#Mastodon
platform_mastodon = tk.Label(window, text="Mastodon User Search")
platform_mastodon.grid(row=0, column=2)
platform_mastodon_user = tk.Entry(window)
platform_mastodon_user.grid(row=1, column=2)

# Create the button to trigger the request
buttonTwitter = tk.Button(window, text="Get Result", command=on_click_twitter)
buttonTwitter.grid(row=2, column=0)

buttonInstagram = tk.Button(window, text="Get Result", command=on_click_instagram)
buttonInstagram.grid(row=2, column=1)

buttonMastodon = tk.Button(window, text="Get Result", command=on_click_mastodon)
buttonMastodon.grid(row=2, column=2)

# # Create the text box to display the result
textbox_twitterUsers = tk.Text(window, width=60, height=50)
textbox_twitterUsers.grid(row=6, column=0)
#
textbox_instagramUsers = tk.Text(window, width=60, height=50)
textbox_instagramUsers.grid(row=6, column=1)
#
textbox_mastodonUsers = tk.Text(window, width=60, height=50)
textbox_mastodonUsers.grid(row=6, column=2)

buttons_twitter = []
buttons_instagram = []
buttons_mastodon = []

window.mainloop()


