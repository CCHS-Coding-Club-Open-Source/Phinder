#!/usr/bin/env python3

import os
import sys
import json
import urllib.request

tzLongDict = {"CEST": "Europe/Paris", "CDT": -90, "EET": "Europe/Athens", "CET": "Europe/Paris", "KST": "Asia/Seoul", "CLT": "America/Santiago", "HST": "Pacific/Honolulu", "CST": -90, "CAT": "Africa/Harare", "BRT": "America/Sao_Paulo", "JST": "Asia/Tokyo", "GST": "Asia/Dubai", "PHT": "Asia/Manila", "BST": "Europe/London", "PST": -120, "ART": "America/Argentina/Buenos_Aires", "WAT": "Africa/Lagos", "EST": -75, "BDT": "Asia/Dhaka", "TRT": "Europe/Istanbul", "CLST": "America/Santiago", "AKST": "America/Juneau", "PKT": "Asia/Karachi", "ICT": "Asia/Bangkok", "MSK": "Europe/Moscow", "EAT": "Africa/Addis_Ababa", "WEST": "Europe/Lisbon", "BRST": "America/Sao_Paulo", "EEST": "Europe/Athens", "MSD": "Europe/Moscow", "MST": 105, "NZDT": "Pacific/Auckland", "PET": "America/Lima", "NST": "America/St_Johns", "NDT": "America/St_Johns", "MDT": 105, "NZST": "Pacific/Auckland", "COT": "America/Bogota", "WET": "Europe/Lisbon", "SGT": "Asia/Singapore", "IST": "Asia/Kolkata", "HKT": "Asia/Hong_Kong", "UTC": "UTC", "EDT": -75, "WIT": "Asia/Jakarta", "IRST": "Asia/Tehran", "AKDT": "America/Juneau", "PDT": -120, "ADT": "America/Halifax", "AST": "America/Halifax", "GMT": "GMT"}

tz = input("Enter timezone code:\n").upper()
cal = input("Enter Calendar:\n")
# time = input("Enter device time as 'min:sec'\n").split(':') # No real use right now, since we have the zones
region = input("Enter region code:\n")
ssid = input("Enter SSID:\n")
ip = input("Enter IP address:\n")

# barPressure = float(input("Enter barometric pressure:\n"))
# heading = float(input("Enter device's compass heading:\n"))
# accel = float(input("Enter device's accelerometer reading\n"))


# Ordering of data:
# 1: Time (Compare to current world times to find phone's timezone.)
# 2 Movement (Compass + directional accelerometer to determine if the phone is moving and in what direction)
# 3 Wi-Fi location (Find list of wifi signals meeting the pre-determined criteria
# 4 Barometer (Match those wi-fi signals to the given height of the phone.)

lat = 0
lng = 0


lng = tzLongDict[tz]

print("Timezone Longitude (deg):", lng)


# # Here we would look-up Wi-Fi SSID and save to file (not done programmatically for now because of query caps) # #


ssidFilePath = os.path.normpath(sys.path[0] + "/Wi-Fi Lookups/" + ssid + ".json")
ssidFile = open(ssidFilePath)
ssidInfoJson = ssidFile.read()
ssidFile.close()

ssidInfoDict = json.loads(ssidInfoJson)

print("ssidInfoDict from lookup:", ssidInfoDict)

ssidResults = ssidInfoDict['results']
ssidLats = []
ssidLongs = []

for result in ssidResults:
    ssidLats.append(result['trilat'])
    ssidLongs.append(result['trilong'])

print("ssidLats:", ssidLats)
print("ssidLongs:", ssidLongs)


ssidLongs2 = []

for lo in ssidLongs:
    if abs(lo - lng) < 15:
        ssidLongs2.append(lo)


print("ssidLongs2:", ssidLongs2)

ssidResults2 = []

for result in ssidResults:
    if result['trilong'] in ssidLongs2:
        ssidResults2.append(result)

print(ssidResults2)

for result in ssidResults2:
    print(result['housenumber'], result['road'], result['city'], result['country'])

# f = urllib.request.urlopen("http://ip-api.com/json/" + ip)
# ipInfoJson = f.read().decode('utf-8')
#
# ipInfoDict = json.loads(ipInfoJson)
# print(ipInfoDict)
#
# ipLat = ipInfoDict['lat']
# ipLong = ipInfoDict['lon']
#
# ssidLongClosestToIp = ssidLongs2[min(range(len(ssidLongs2)), key=lambda i: abs(ssidLongs2[i]-ipLong))]
#
# print(ssidLongClosestToIp)