from flask import Flask, render_template, json, request
import RPi.GPIO as GPIO
from time import sleep
import os
import _thread

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)
GPIO.setwarnings(False)

flask_app = Flask(__name__)

button1 = ""
button2 = ""
button3 = ""
button4 = ""
button5 = ""
button6 = ""

@flask_app.route('/')
def main():
    return render_template('index.html')

@flask_app.route('/jam/', methods=['POST','GET'])
def jam():
    global choice
    sound = request.form.get('sound')
    print("stuff happening")
    if sound == 'Theme1':
        button1 = "static/sounds/aaahMadeon"
        button2 = "static/sounds/clap.mp3"
        button3 = "static/sounds/freezeIntroAudio.mp3"
        button4 = "static/sounds/mario.mp3"
        button5 = "static/sounds/midifreeze.mp3"
        button6 = "static/sounds/over.mp3"
    elif sound == 'Theme2':
        button1 = ""
        button2 = ""
        button3 = ""
        button4 = ""
        button5 = ""
        button6 = ""
    elif sound == 'Theme3':
        button1 = ""
        button2 = ""
        button3 = ""
        button4 = ""
        button5 = ""
        button6 = ""

    return render_template('jam.html',**locals())

def buttons():
    while True:
        if(GPIO.input(23) == False):
            os.system('mpg123 -q ' + button1 + ' &')
        sleep(0.1)
        if(GPIO.input(24) == False):
            os.system('mpg123 -q ' + button2 + ' &')
        sleep(0.1)
        if(GPIO.input(25) == False):
            os.system('mpg123 -q ' + button3 + ' &')
        sleep(0.1)
        if(GPIO.input(12) == False):
            os.system('mpg123 -q ' + button4 + ' &')
        sleep(0.1)
        if(GPIO.input(16) == False):
            os.system('mpg123 -q ' + button5 + ' &')
        sleep(0.1)
        if(GPIO.input(23) == False):
            os.system('mpg123 -q ' + button6 + ' &')
        sleep(0.1)
    #return 1



if __name__ == "__main__":
    _thread.start_new_thread(buttons,())
    flask_app.run(host='198.21.247.207')
