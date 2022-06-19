#!/bin/env python3
from flask import Flask, render_template, request, url_for, flash, redirect
import requests
app = Flask(__name__)


messages = []

@app.route('/')
def index():
    return render_template('index.html', messages=messages)

@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        ville = request.form['ville']

        if not ville:
            flash('City is required!')
        else:
            
            r = requests.get(url='https://api.openweathermap.org/data/2.5/weather?q='+ville+'&appid=f1c88735ef0dd89daeca72047b77fdb2')
            data =r.json()
            temp = data["main"]["temp"]
            temp_min = data["main"]["temp_min"]
            temp_max = data["main"]["temp_max"]
            pressure = data["main"]["pressure"]
            humidity = data["main"]["humidity"]
            main = data["weather"][0]["main"]
            description = data["weather"][0]["description"]
            messages.append({'ville': ville, 'temperature': temp,'temperature_min': temp_min,'temperature_max': temp_max,'pression': pressure, 'humidite': humidity, 'main': main, 'description' : description})
            return redirect(url_for('index'))

    return render_template('create.html')






print("PATH =====>", app.instance_path)
if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.secret_key = 'chooseaverysecretkeyhere'
    app.run(host='0.0.0.0', port=5000)