import RPi.GPIO as IO

#pin locations, the BCM pin numbers
x_pin = 19
y_pin = 20
z_pin = 21
maxFreq = 1000 #measured in hertz
maxCurrent = 100 #AMPs?
scaleDC = 0x7FFFF

IO.setmode(IO.BCM) # this just makes it so pin numbers are by the BCM pin nums so 'GPIO19' instead of pin 35

#initializing the output pins
IO.setup(x_pin, IO.OUT) 
IO.setup(y_pin, IO.OUT)
IO.setup(z_pin, IO.OUT)

#setting up the output pins as pwm output, and the max frequency
a = IO.PWM(x_pin, IO.OUT)
b = IO.PWM(y_pin, IO.OUT)
c = IO.PWM(z_pin, IO.OUT)

#generating/initializing the PWM signal for each axis, starting with 0% duty cycle
a.start(0)
b.start(0)
c.start(0)

def controlPWM(x, y, z):
    try:
        if x != 0:
            a.ChangeDutyCycle(calcDC(x))

        if y != 0:
            b.ChangeDutyCycle(calcDC(y))

        if z != 0:
            c.ChangeDutyCycle(calcDC(z))

        printMags(x, y, z) #Used for testing

    except Exception as e: # IMPORTANT TO ALWAYS RESET MAGNETORQUER VALUES TO ZERO.
        print(e)
        resetDutyCycles()

def printMags(x, y, z):
    print('MAGS VALUES:')
    print('x: ' + calcDC(x))
    print('y: ' + calcDC(y))
    print('z: ' + calcDC(z))

def calcDC(current):
    # FOR TESTING MAY WANT TO SCALE DOWN DUTY CYCLE at first
    if current > maxCurrent:
        return scaleDC
    else:
        return current / maxCurrent * scaleDC
      
def resetDutyCycles():
    a.ChangeDutyCycle(0)
    b.ChangeDutyCycle(0)
    c.ChangeDutyCycle(0)
