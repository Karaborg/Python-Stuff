# CONTROLLING THE RELAY MODULE

# Jumper Cable Colors:
#	ORANGE, RED, BLUE, BROWN, BLACK, WHITE and GREY

# Raspberry Pi Jumper Placements:
#	RED - 1
#	ORANGE - 2
#	BLUE - 32
#	BLACK - 34
#	GREY - 36
#	WHITE - 38
#	BROWN - 40

# Relay Module Jumper Placements:
#	RED - VCC (The one with next to JD-VCC)
#	ORANGE - JD-VCC
#	BLACK - GRD
#	BLUE - IN1
#	GREY - IN2
#	WHIRE - IN3
#	BROWN - IN4

# To Run, Type: "python relay.py"

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

GPIO.setup(32,GPIO.OUT)
GPIO.output(32,GPIO.HIGH)

GPIO.setup(36,GPIO.OUT)
GPIO.output(36,GPIO.HIGH)

GPIO.setup(38,GPIO.OUT)
GPIO.output(38,GPIO.HIGH)

GPIO.setup(40,GPIO.OUT)
GPIO.output(40,GPIO.HIGH)

try:
	GPIO.output(32,GPIO.LOW)
	print("First Relay ON")
	time.sleep(2)
	GPIO.output(36,GPIO.LOW)
        print("Second Relay ON")
        time.sleep(2)
	GPIO.output(38,GPIO.LOW)
        print("Third Relay ON")
        time.sleep(2)
	GPIO.output(40,GPIO.LOW)
        print("Fourth Relay ON")
        time.sleep(5)
	GPIO.cleanup()
	print("ALL OFF.....Good Bye !!!")

except KeyboardInterrupt:
	print("QUIT")
	GPIO.cleanup()
