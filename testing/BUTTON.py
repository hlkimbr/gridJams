import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17,GPIO.OUT)
GPIO.setwarnings(False)

light_on = False;
while True:
    input_state = GPIO.input(18)
    if input_state == False and light_on == False:
	GPIO.output(17,GPIO.HIGH)
	time.sleep(0.2)
        print('Button Pressed and Light On')
	light_on = True
    elif input_state ==  False and light_on == True:
	GPIO.output(17,GPIO.LOW)
	time.sleep(0.2)
	light_on = False
	print('Button Pressed and Light Off')
    
	
