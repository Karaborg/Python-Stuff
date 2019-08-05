import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM) #GPIO Numbers instead of board numbers

RELAY = 17

GPIO.setwarnings(False)

GPIO.setup(RELAY, GPIO.OUT) #GPIO Assign Mode
GPIO.output(RELAY, GPIO.LOW) #OUT
GPIO.output(RELAY, GPIO.HIGH) #ON
GPIO.cleanup()
