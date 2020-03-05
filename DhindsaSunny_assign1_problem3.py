#design a program that converts 4500 in into different measurements
#format properly
print("--------------------------------------------------------------")
#create title string
title = "Inches to Centimeters"
#create string to format title properly to the right > = how many characters string is
fTitle = format(title, ">37s" ) 
print(fTitle)
print("--------------------------------------------------------------")
#create strings for each of the conversion types
inch = "in:"
feet = "ft:"
yard = "yd:"
miles = "mi"
kilometer = "km:"
meter = "m:"
centimeter = "cm:"
#format each of the strings so they're 10 characters in length to the right
fInch = format(inch, ">10s")
fFeet = format(feet, ">10s")
fYard = format(yard, ">10s")
fMiles = format(miles, ">10s")
fKilometer = format(kilometer, ">10s")
fMeter = format(meter, ">10s")
fCentimeter = format(centimeter, ">10s")
#create formulas to convert each float from 4500 inches using conversion chart
cInch = 4500.0
cFt = cInch/12
cYd = cFt/3
cMiles = cYd/1760
cKilometers = cMiles*1.60934
cMeter = cKilometers*1000
cCentimeters = cMeter*100
#convert each float (which we did operations on) to string so we can later format it
stringCInch = str(cInch)
stringCFt = str(cFt)
stringCYd = str(cYd)
stringCMiles = str(cMiles)
stringCKilometers = str(cKilometers)
stringCMeter = str(cMeter)
stringCCentimeters = str(cCentimeters)
#create strings to format each of the now converted from float data types
fCInch = format(stringCInch, ">20s")
fCFeet = format(stringCFt, ">19s")
fCYd = format (stringCYd, ">19s")
fCMiles = format(stringCMiles, ">33s")
fCKilometer = format(stringCKilometers, ">33s")
fCMeter = format(stringCMeter, ">32s")
fCCentimeter = format(stringCCentimeters, ">32s")
#on the same line, print the formatted strings as well as formatted conversions
print(fInch, fCInch)
print(fFeet, fCFeet)
print(fYard, fCYd)
print(fMiles, fCMiles)
print(fKilometer, fCKilometer)
print(fMeter, fCMeter)
print(fCentimeter, fCCentimeter)

