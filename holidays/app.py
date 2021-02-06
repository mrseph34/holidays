from flask import Flask, render_template, json, jsonify, request, current_app as app
from datetime import date
import os
import requests

app = Flask(__name__, static_folder="static")

@app.route('/')
def index():
 return render_template('index.html')

@app.route('/holidays')
def holidays():
 response = requests.get('https://date.nager.at/api/v2/publicholidays/2021/US')
 
 data = response.json()
 
 return render_template('home.html',data=data)

@app.route('/holidays/search', methods=['GET'])
def search_title():
    results = []
    response = requests.get('https://date.nager.at/api/v2/publicholidays/2021/US')
    data = response.json()

    if 'title' in request.args:
        title = request.args['title']
        
        for i in data:
            if title in i['name']:
                results.append(i)
            elif title in i['localName']:
                results.append(i)

    if len(results) < 1:
        return "No results found"
    return render_template("home.html", data=results)

if __name__ == '__main__':
 app.run(debug=True, host='0.0.0.0') 