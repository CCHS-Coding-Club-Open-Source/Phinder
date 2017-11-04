#!/usr/bin/env python3

barPressure = float(input("Enter barometric pressure:\n"))
time = input("Enter device time as 'min:sec'\n").split(':')
heading = float(input("Enter device's compass heading:\n"))
currentSpeed = float(input("Enter device's current speed\n"))


print("Hello world!")

print(barPressure, time, heading, currentSpeed)
