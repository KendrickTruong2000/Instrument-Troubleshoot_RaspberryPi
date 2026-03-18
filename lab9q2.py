import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

LED_PIN = 21
BUTTON_PIN = 16
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN)

try:
    while True:
        if GPIO.input(BUTTON_PIN) == GPIO.LOW:
            GPIO.output(LED_PIN, GPIO.HIGH)
            print("LED ON")
        else:
            GPIO.output(LED_PIN, GPIO.LOW)
            print("LED OFF")
            
except KeyboardInterrupt:
    GPIO.cleanup()
    print("Program exited")