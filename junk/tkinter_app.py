import tkinter as tk
from tkinter import Tk
import requests

def get_result(name, max_followers, platform):
    # Make a request to the Flask API
    # response = requests.get(f'http://localhost:5000/my_endpoint?param1={param1}&param2={param2}')
    if platform == 'instagram':
        response = requests.get(f'http://127.0.0.1:5000/get_data/instagram?name={name}&max_followers={max_followers}')
    elif platform == 'twitter':
        response = requests.get(f'http://127.0.0.1:5000/get_data/twitter?name={name}&max_followers={max_followers}')
    # response = requests.get(f'http://127.0.0.1:5000/get_data/instagram?name={name}&max_followers={max_followers}')
    # Get the result from the response
    result = response.text
    return result

def on_click():
    # Get the values of the inputs
    name = entry1.get()
    max_followers = entry2.get()
    platform = entry3.get()
    # Call the get_result function and display the result in the text box
    result = get_result(name, max_followers, platform)
    textbox.delete('1.0', tk.END)
    textbox.insert(tk.END, result)

# Create the Tkinter window
window = tk.Tk()
window.title("Social Media App")

# Create the input widgets
label1 = tk.Label(window, text="Screen Name: ")
label1.grid(row=0, column=0)
entry1 = tk.Entry(window)
entry1.grid(row=0, column=1)

label2 = tk.Label(window, text="Max Followers: ")
label2.grid(row=1, column=0)
entry2 = tk.Entry(window)
entry2.grid(row=1, column=1)

label3 = tk.Label(window, text="Platform: ")
label3.grid(row=2, column=0)
entry3 = tk.Entry(window)
entry3.grid(row=2, column=1)

# Create the button to trigger the request
button = tk.Button(window, text="Get Result", command=on_click)
button.grid(row=3, column=0, columnspan=2)

# Create the text box to display the result
textbox = tk.Text(window)
textbox.grid(row=4, column=0, columnspan=2)

# Run the Tkinter event loop
window.mainloop()
