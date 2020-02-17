""" Import statements """
import RPi.GPIO as gpio
import time

""" Pin constants """
PB_IN = 2
PWM_OUT = 20
CW_ONE = 13
CCW_ONE = 19

""" Pin setup """
# Basic setup
gpio.setwarnings(False)
gpio.setmode(gpio.BCM) # use board value 

# Pin assignments
gpio.setup(PB_IN, gpio.IN) # Pin 3: GPIO 2 => Input from pushbutton
gpio.setup(PWM_OUT, gpio.OUT) # Pin 38: GPIO 20 => PWM output
gpio.setup(CW_ONE, gpio.OUT) # Pin 33: GPIO 13 => Direction pin 1: CW
gpio.setup(CCW_ONE, gpio.OUT) # Pin 35: GPIO 19 => Direction pin 2: CCW

""" PWM_OUT setup - to be executed once """
motor = gpio.PWM(PWM_OUT, 100) # set PWM frequency to 100 Hz
motor.start(0) # initialise with 0% duty cycle

""" Helper functions """
def set_pins_false():
    gpio.output(CW_ONE, False)
    gpio.output(CCW_ONE, False)
    
def set_clockwise():
    gpio.output(CW_ONE, True)
    gpio.output(CCW_ONE, False)

""" Routine """
while True:
    
    # check if push button is pressed
    if not gpio.input(PB_IN):
        set_clockwise()
        motor.ChangeDutyCycle(50)
    else:
        set_pins_false()
        motor.ChangeDutyCycle(0)
        
