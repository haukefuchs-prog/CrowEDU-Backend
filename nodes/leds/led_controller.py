import RPi.GPIO as GPIO

LED_BLUE = 19
LED_GREEN = 16
LED_YELLOW = 26
LED_RED = 20

GPIO.setmode(GPIO.BCM)

for pin in [LED_BLUE, LED_GREEN, LED_YELLOW, LED_RED]:
    GPIO.setup(pin, GPIO.OUT)

def all_off():
    global current_led

    for pin in [LED_BLUE, LED_GREEN, LED_YELLOW, LED_RED]:
        GPIO.output(pin, GPIO.HIGH)

def green_on():
    GPIO.output(LED_GREEN, GPIO.LOW)

def green_off():
    GPIO.output(LED_GREEN, GPIO.HIGH)

def blue_on():
    GPIO.output(LED_BLUE, GPIO.LOW)

def blue_off():
    GPIO.output(LED_BLUE, GPIO.HIGH)

def red_on():
    GPIO.output(LED_RED, GPIO.LOW)

def red_off():
    GPIO.output(LED_RED, GPIO.HIGH)

def yellow_on():
    GPIO.output(LED_YELLOW, GPIO.LOW)

def yellow_off():
    GPIO.output(LED_YELLOW, GPIO.HIGH)