# from flask import Flask, render_template, request
# import requests
#
# app = Flask(__name__)
#
# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         first_name = request.form['first_name']
#         last_name = request.form['last_name']
#         response = requests.get('https://backend-service.com/api/names', params={'first_name': first_name, 'last_name': last_name})
#         names = response.json()['names']
#         return render_template('index.html', names=names)
#     else:
#         return render_template('index.html')
#
# if __name__ == '__main__':
#     app.run()


import tkinter as tk

root = tk.TK()

root.mainloop()

