import tkinter as tk
import tkinter.font as tkFont

x_pwm = 1
y_pwm = 1
z_pwm = 1

step = 1

root = tk.Tk()

def increment_x():
    global x_pwm
    x_pwm += step
    x_txt.set(x_pwm)

def decrement_x():
    global x_pwm
    x_pwm -= step
    x_txt.set(x_pwm)

def increment_y():
    global y_pwm
    y_pwm += step
    y_txt.set(y_pwm)

def decrement_y():
    global y_pwm
    y_pwm -= step
    y_txt.set(y_pwm)

def increment_z():
    global y_pwm
    y_pwm += step
    y_txt.set(y_pwm)

def decrement_z():
    global z_pwm
    z_pwm -= step
    z_txt.set(z_pwm)

font = tkFont.Font(family="Arial", size=50)

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

root.mainloop()