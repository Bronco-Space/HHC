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

    dutyCycleChange()

def decrement_x():
    global x_pwm

    if x_pwm > -10:
        x_pwm -= step

    dutyCycleChange()

def increment_y():
    global y_pwm

    if y_pwm < 10:
        y_pwm += step

    dutyCycleChange()

def decrement_y():
    global y_pwm

    if y_pwm > -10:
        y_pwm -= step

    dutyCycleChange()

def increment_z():
    global z_pwm

    if z_pwm < 10:
        z_pwm += step

    dutyCycleChange()

def decrement_z():
    global z_pwm

    if z_pwm > -10:
        z_pwm -= step
        z_txt.set(z_pwm)
    
    dutyCycleChange()

def calcDC(current):
    # FOR TESTING MAY WANT TO SCALE DOWN DUTY CYCLE at first
    current = abs(current)
    if current > maxCurrent:
        return scaleDC
    else:
        return current / maxCurrent * scaleDC

def stop():
    global x_pwm, y_pwm, z_pwm
    x_pwm=0
    y_pwm=0
    z_pwm=0
    dutyCycleChange()

def resetDutyCycles():
    global a,b,c
    a.ChangeDutyCycle(0)
    b.ChangeDutyCycle(0)
    c.ChangeDutyCycle(0)


def dutyCycleChange():
    print("updating")
    global a,b,c,x_pwm,y_pwm,z_pwm
    
    x_txt.set(x_pwm)
    y_txt.set(y_pwm)
    z_txt.set(z_pwm)

    a.ChangeDutyCycle(calcDC(x_pwm))
    b.ChangeDutyCycle(calcDC(y_pwm))
    c.ChangeDutyCycle(calcDC(z_pwm))
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


font = tkFont.Font(family="Arial", size=100)

x_inc = tk.Button(root, text="x+", command=increment_x, font=font)
x_inc.grid(row=1, column=1)
x_txt = tk.StringVar()
x_txt.set(x_pwm)
x_label = tk.Label(root, textvariable=x_txt, font=font)
x_label.grid(row=2,column=1)
x_dec = tk.Button(root, text="x-", command=decrement_x, font=font)
x_dec.grid(row=3, column=1)

y_inc = tk.Button(root, text="y+", command=increment_y, font=font)
y_inc.grid(row=1, column=2)
y_txt = tk.StringVar()
y_txt.set(y_pwm)
y_label = tk.Label(root, textvariable=y_txt, font=font)
y_label.grid(row=2,column=2)
y_dec = tk.Button(root, text="y-", command=decrement_y, font=font)
y_dec.grid(row=3, column=2)

z_inc = tk.Button(root, text="z+", command=increment_z, font=font)
z_inc.grid(row=1, column=3)
z_txt = tk.StringVar()
z_txt.set(z_pwm)
z_label = tk.Label(root, textvariable=z_txt, font=font)
z_label.grid(row=2,column=3)
z_dec = tk.Button(root, text="z-", command=decrement_z, font=font)
z_dec.grid(row=3, column=3)

stop = tk.Button(root, text="STOP", command=stop, font=font)
stop.grid(row=2, column=4)

root.mainloop()

print("exiting")
IO.cleanup()