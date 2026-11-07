import RPi.GPIO as GPIO

LED_BLUE = 19
LED_GREEN = 16
LED_YELLOW = 26
LED_RED = 20

current_led = "none"


GPIO.setmode(GPIO.BCM)

for pin in [LED_BLUE, LED_GREEN, LED_YELLOW, LED_RED]:
    GPIO.setup(pin, GPIO.OUT)

def all_off():
    global current_led

    for pin in [LED_BLUE, LED_GREEN, LED_YELLOW, LED_RED]:
        GPIO.output(pin, GPIO.HIGH)

    current_led = "none"

def green_on():
    global current_led

    all_off()
    GPIO.output(LED_GREEN, GPIO.LOW)
    current_led = "green"

def yellow_on():
    global current_led

    all_off()
    GPIO.output(LED_YELLOW, GPIO.LOW)
    current_led = "yellow"

def red_on():
    global current_led

    all_off()
    GPIO.output(LED_RED, GPIO.LOW)
    current_led = "red"

def blue_on():
    global current_led

    all_off()
    GPIO.output(LED_BLUE, GPIO.LOW)
    current_led = "blue"