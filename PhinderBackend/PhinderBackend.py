#!/usr/bin/env python3

barPressure = float(input("Enter barometric pressure:\n"))
time = input("Enter device time as 'min:sec'\n").split(':') #time zones
heading = float(input("Enter device's compass heading:\n"))
accel = float(input("Enter device's accelerometer reading\n"))


print("Hello world!")

print(barPressure, time, heading, accel)
