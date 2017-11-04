#!/usr/bin/env python3

tz = input("Enter timezone:\n")
cal = input("Enter Calendar:\n")
# time = input("Enter device time as 'min:sec'\n").split(':') # No real use right now, since we have the zones
region = input("Enter region code:\n")
ssid = input("Enter SSID:\n")

# barPressure = float(input("Enter barometric pressure:\n"))
# heading = float(input("Enter device's compass heading:\n"))
# accel = float(input("Enter device's accelerometer reading\n"))


# Ordering of data:
# 1: Time (Compare to current world times to find phone's timezone.)
# 2 Movement (Compass + directional accelerometer to determine if the phone is moving and in what direction)
# 3 Wi-Fi location (Find list of wifi signals meeting the pre-determined criteria
# 4 Barometer (Match those wi-fi signals to the given height of the phone.)

