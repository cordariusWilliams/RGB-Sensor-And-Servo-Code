# Write your code here :-)

import time

import pwmio
from adafruit_motor import servo
import board
import busio


import adafruit_tcs34725


##################
# *EDIT*
# Set configurable values below
# Feed name for Adafruit IO

# milliseconds to gather color data
sensor_integration_time = 150

# manually override the color sensor gain
sensor_gain = 4

# Collect this many samples each time we prompt the user
num_samples = 5

#
# End of editable config values
##################

# Create sensor object, communicating over the board's default I2C bus
i2c = busio.I2C(board.GP3, board.GP2)  # uses first I2C SCA/SCL pair on pico
sensor = adafruit_tcs34725.TCS34725(i2c)

# Change sensor gain to 1, 4, 16, or 60
sensor.gain = sensor_gain
# Change sensor integration time to values between 2.4 and 614.4 milliseconds
sensor.integration_time = sensor_integration_time

# create a PWMOut object on Pin A2.
pwm = pwmio.PWMOut(board.GP22, duty_cycle=2 ** 15, frequency=50)
pwm2 = pwmio.PWMOut(board.GP21, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)
my_servo2 = servo.Servo(pwm2)

while True:
    my_servo.angle = 0
    time.sleep(2)
    my_servo.angle = 180
    time.sleep(2)
    my_servo2.angle = 0
    time.sleep(2)
    my_servo2.angle = 180
    time.sleep(2)






    time.sleep(1)
    print("Temperature: %d" % sensor.color_temperature)
    print(
        "r: %d, g: %d, b: %d"
        % (
            sensor.color_rgb_bytes[0],
            sensor.color_rgb_bytes[1],
            sensor.color_rgb_bytes[2],
        )
    )
    print("Lux: %d" % sensor.lux)
