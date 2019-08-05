import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM) #GPIO Numbers instead of board numbers

GPIO.setwarnings(False)

Relay = 17
GPIO.setup(Relay,GPIO.OUT)

GPIO.output(Relay,GPIO.HIGH)
#GPIO.cleanup()
