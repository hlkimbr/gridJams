from flask import Flask, render_template, json, request
# import RPi.GPIO as GPIO
# from time import sleep

# GPIO.setmode(GPIO.BCM)
# GPIO.setup(23, GPIO.IN)
# GPIO.setwarnings(False)

app = Flask(__name__)

choice = "Marbles"

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/jam/', methods=['POST','GET'])
def jam():
    sound = request.form.get('sound')
    print("stuff happening")
    if sound == 'Airplane':
        choice = 'sounds/airplane.mp3'
    elif sound == 'Boomerang':
        choice = 'sounds/Boomerang.mp3'
    else:
        choice = 'sounds/marbles.mp3'

    return render_template('jam.html',**locals())

@app.route('/jam/temp')
def temp():
    while True:
        if(GPIO.input(23) == False):
            os.system('mpg123 -q ' + choice + ' &')
        sleep(0.1);
    return render_template('jam.html',**locals())

if __name__ == "__main__":
    app.run()
