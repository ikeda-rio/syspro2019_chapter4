import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
servo = GPIO.PWM(2, 50)
servo.start(0.0)

bottom = 2.5
middle = 7.2
top = 12.0

for i in range(5):
	servo.ChangeDutyCycle(bottom)
	time.sleep(1.0)

	servo.ChangeDutyCycle(middle)
	time.sleep(1.0)

	servo.ChangeDutyCycle(top)
	time.sleep(1.0)
	

def setservo(kakudo):
	nanika = (1.9*(kakudo+90)/180+0.5)/20*100
	servo.ChangeDutyCycle(nanika)
	time.sleep(1.0)

setservo(90.0)
setservo(-90.0)

GPIO.cleanup()
