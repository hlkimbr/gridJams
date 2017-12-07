from flask import Flask, render_template, json, request
import RPi.GPIO as GPIO
from time import sleep
import os
import _thread

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)
GPIO.setup(25, GPIO.IN)
GPIO.setup(12, GPIO.IN)
GPIO.setup(16, GPIO.IN)
GPIO.setup(20, GPIO.IN)
#GPIO.setwarnings(False)

flask_app = Flask(__name__)

button1 = ""#"static/sounds/aaahMadeon.mp3"
button2 = ""#"static/sounds/clap.mp3"
button3 = ""#"static/sounds/freezeIntroAudio.mp3"
button4 = ""#"static/sounds/mario.mp3"
button5 = ""#"static/sounds/midifreeze.mp3"
button6 = ""#static/sounds/over.mp3"

@flask_app.route('/')
def main():
    return render_template('index.html')

@flask_app.route('/jam/', methods=['POST','GET'])
def jam():
    global button1
    global button2
    global button3
    global button4
    global button5
    global button6
    sound = request.form.get('sound')
    print("stuff happening")
    if sound == 'Theme1':
        button1 = "static/sounds/3setsOfTracks/set1/set1track1.mp3"
        button2 = "static/sounds/3setsOfTracks/set1/set1track2.mp3"
        button3 = "static/sounds/3setsOfTracks/set1/set1track3.mp3"
        button4 = "static/sounds/3setsOfTracks/set1/set1track4.mp3"
        button5 = "static/sounds/3setsOfTracks/set1/set1track5.mp3"
        button6 = "static/sounds/3setsOfTracks/set1/set1track6.mp3"
    elif sound == 'Theme2':
        button1 = "static/sounds/3setsOfTracks/set2/set2track1.mp3"
        button2 = "static/sounds/3setsOfTracks/set2/set2track2.mp3"
        button3 = "static/sounds/3setsOfTracks/set2/set2track3.mp3"
        button4 = "static/sounds/3setsOfTracks/set2/set2track4.mp3"
        button5 = "static/sounds/3setsOfTracks/set2/set2track5.mp3"
        button6 = "static/sounds/3setsOfTracks/set2/set2track6.mp3"
    elif sound == 'Theme3':
        button1 = "static/sounds/3setsOfTracks/set3/set3track1.mp3"
        button2 = "static/sounds/3setsOfTracks/set3/set3track2.mp3"
        button3 = "static/sounds/3setsOfTracks/set3/set3track3.mp3"
        button4 = "static/sounds/3setsOfTracks/set3/set3track4.mp3"
        button5 = "static/sounds/3setsOfTracks/set3/set3track5.mp3"
        button6 = "static/sounds/3setsOfTracks/set3/set3track6.mp3"

    return render_template('jam.html',**locals())

def buttons():
    while True:
        if(GPIO.input(23) == False):
            os.system('mpg123 -q ' + button1 + ' &')
        if(GPIO.input(24) == False):
             os.system('mpg123 -q ' + button2 + ' &')
        if(GPIO.input(25) == False):
             os.system('mpg123 -q ' + button3 + ' &')
        if(GPIO.input(12) == False):
             os.system('mpg123 -q ' + button4 + ' &')
        if(GPIO.input(16) == False):
             os.system('mpg123 -q ' + button5 + ' &')
        if(GPIO.input(20) == False):
             os.system('mpg123 -q ' + button6 + ' &')

        sleep(0.1);

if __name__ == "__main__":
    _thread.start_new_thread(buttons,())
    flask_app.run(host='198.21.240.188')
