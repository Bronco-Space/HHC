import tkinter as tk
import tkinter.font as tkFont
import RPi.GPIO as IO

#pin locations, the BCM pin numbers
x_pin = 19
y_pin = 20
z_pin = 21
x_dir_pin = 26
y_dir_pin = 16
z_dir_pin = 6
maxFreq = 20 #measured in hertz
maxCurrent = 10 #AMPs?
scaleDC = 100

IO.setmode(IO.BCM) # this just makes it so pin numbers are by the BCM pin nums so 'GPIO19' instead of pin 35

#initializing the output pins
IO.setup(x_pin, IO.OUT) 
IO.setup(y_pin, IO.OUT)
IO.setup(z_pin, IO.OUT)

IO.setup(x_dir_pin, IO.OUT) 
IO.setup(y_dir_pin, IO.OUT)
IO.setup(z_dir_pin, IO.OUT)

#setting up the output pins as pwm output, and the max frequency
a = IO.PWM(x_pin, maxFreq)
b = IO.PWM(y_pin, maxFreq)
c = IO.PWM(z_pin, maxFreq)

#generating/initializing the PWM signal for each axis, starting with 0% duty cycle
a.start(0)
b.start(0)
c.start(0)

x_pwm = 0
y_pwm = 0
z_pwm = 0

step = 1

root = tk.Tk()

def increment_x():
    global x_pwm
    if x_pwm < 10:     
        x_pwm += step

def decrement_x():
    global x_pwm

    if x_pwm > -10:
        x_pwm -= step

def increment_y():
    global y_pwm

    if y_pwm < 10:
        y_pwm += step

def decrement_y():
    global y_pwm

    if y_pwm > -10:
        y_pwm -= step

def increment_z():
    global z_pwm

    if z_pwm < 10:
        z_pwm += step

def decrement_z():
    global z_pwm

    if z_pwm > -10:
        z_pwm -= step

def calcDC(current):
    # FOR TESTING MAY WANT TO SCALE DOWN DUTY CYCLE at first
    if current > maxCurrent:
        return scaleDC
    else:
        return current / maxCurrent * scaleDC

def stop():
    global x_pwm, y_pwm, z_pwm
    resetDutyCycles()
    x_pwm=0
    y_pwm=0
    z_pwm=0

def resetDutyCycles():
    global a,b,c
    a.ChangeDutyCycle(0)
    b.ChangeDutyCycle(0)
    c.ChangeDutyCycle(0)

def printMags(x, y, z):
    print('MAGS VALUES:')
    print('x: ' + calcDC(x))
    print('y: ' + calcDC(y))
    print('z: ' + calcDC(z))

def dutyCycleChange():
    global a,b,c,x_pwm,y_pwm,z_pwm
    a.ChangeDutyCycle(abs(x_pwm))
    b.ChangeDutyCycle(abs(y_pwm))
    c.ChangeDutyCycle(abs(z_pwm))
    printMags(x_pwm,y_pwm,z_pwm)
    if x_pwm<0:
        IO.output(x_dir_pin, True)
    else:
        IO.output(x_dir_pin, False)
    
    if y_pwm<0:
        IO.output(y_dir_pin, True)
    else:
        IO.output(y_dir_pin, False)

    if z_pwm<0:
        IO.output(z_dir_pin, True)
    else:
        IO.output(z_dir_pin, False)

IO.cleanup()