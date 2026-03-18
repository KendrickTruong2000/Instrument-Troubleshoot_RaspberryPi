import RPi.GPIO as GPIO
import time

# Set up the GPI pin numbering mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

LED_PIN = 21
GPIO.setup(LED_PIN, GPIO.OUT)

try:
    while True:
        print("LED on")
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(1)
        print("LED off")
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(1)
        
except KeyboardInterrupt:
    # Clean up the GPIO pins on exit
    GPIO.cleanup()
    print("Program exited cleanly")
