import RPi.GPIO as gpio
gpio.setmode(gpio.BOARD)
class Wheel(object):
    def __init__(self, in_pin1, in_pin2, in_pin3, in_pin4, enable_pin1, enable_pin2):
        '''
        :param in_pin1 in_pin2: IN1 IN2 or IN3 IN4
        :param enable_pin1 enable_pin2: ENA or ENB
        '''
        self.pin1 = in_pin1
        self.pin2 = in_pin2
        self.pin3 = in_pin3
        self.pin4 = in_pin4

        # setup I/O OUT
        gpio.setup(in_pin1, gpio.OUT)
        gpio.setup(in_pin2, gpio.OUT)
        gpio.setup(in_pin3, gpio.OUT)
        gpio.setup(in_pin4, gpio.OUT)
        gpio.setup(enable_pin1, gpio.OUT)
        gpio.setup(enable_pin2, gpio.OUT)

        # enable
        gpio.output(enable_pin1, True)
        gpio.output(enable_pin2, True)

    def forward(self):
        gpio.output(self.pin1, True)
        gpio.output(self.pin3, True)
        gpio.output(self.pin2, False)
        gpio.output(self.pin4, False)

    def backward(self):
        gpio.output(self.pin2, True)
        gpio.output(self.pin4, True)
        gpio.output(self.pin1, False)
        gpio.output(self.pin3, False)

    def stop(self):
        gpio.output(self.pin1, False)
        gpio.output(self.pin2, False)
        gpio.output(self.pin3, False)
        gpio.output(self.pin4, False)

    def turn_left(self):
        gpio.output(self.pin1, True)
        gpio.output(self.pin2, False)
        gpio.output(self.pin3, False)
        gpio.output(self.pin4, False)

    def turn_right(self):
        gpio.output(self.pin1, False)
        gpio.output(self.pin2, False)
        gpio.output(self.pin3, True)
        gpio.output(self.pin4, False)
wheel_controller=Wheel(11,12,13,15,16,18)
