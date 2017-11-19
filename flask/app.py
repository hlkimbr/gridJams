from flask import Flask, render_template, json, request
import RPi.GPIO as GPIO
from time import sleep
import os
import _thread

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)
GPIO.setwarnings(False)

flask_app = Flask(__name__)

choice = ""

@flask_app.route('/')
def main():
    return render_template('index.html')

@flask_app.route('/jam/', methods=['POST','GET'])
def jam():
    global choice
    sound = request.form.get('sound')
    print("stuff happening")
    if sound == 'Airplane':
        choice = 'static/sounds/airplane.mp3'
    elif sound == 'Boomerang':
        choice = 'static/sounds/Boomerang.mp3'
    elif sound == 'Marbles':
        choice = 'static/sounds/marbles.mp3'
	
    return render_template('jam.html',**locals())

def temp():
    while True:
    #print("YO")
        if(GPIO.input(23) == False):
            os.system('mpg123 -q ' + choice + ' &')
        sleep(0.1)
    #return 1
 
	

if __name__ == "__main__":
    _thread.start_new_thread(temp,())
    flask_app.run(host='198.21.247.207')
