'''Sunny Dhindsa sd3692
CSCI.0002-004 Dakota Hernandez
Assignment 2, problem 3 due 22 Sept 2019
'''
#Data size converter. Prompts user to enter kb data size and converts it

#1. runtime error would occur if user entered in string literal, not number
kbInput = float(input("Enter a file size, in kilobytes (KB): "))
print("")
print(kbInput, "KB ...","\n")
#store conversion variables for bites, bytes, megabytes, and gigabytes

#2. runtime error would occur if I called to variable that didn't exist i.e KBInput instead of kbInput
toBytes = kbInput*1024
toBits = toBytes*8
toMB = kbInput/1024
toGB = toMB/1024

#convert to string and format string to two decimal points
#3. logic error would occur if I didn't have comma separators
#4. logic error if I put .3 decimal places instead of .2 
toBitsString = str(format(toBits, ",.2f"))
toBytesString = str(format(toBytes, ",.2f"))
toMBString = str(format(toMB, ",.2f"))
toGBString = str(format(toGB, ",.2f"))

#format each now converted string to push to the right & be about 30 characters
#5. syntax error if I mispelled format to frmat 

toBitsFormat = format(toBitsString, ">27s")
toBytesFormat = format(toBytesString, ">26s")
toMBFormat = format(toMBString, ">22s")
toGBFormat = format(toGBString, ">22s")

#format conversion types as strings and format them over
bitsString = "bits"
bytesString = "bytes"
MBString = "MB"
GBString = "GB"
formatBitsString = format(bitsString, "<12s")
formatBytesString = format(bytesString, "<12s")
formatMBString = format(MBString, "<2s")
formatGBString = format(GBString, "<2s")

#print each of the conversions
print("... in bits", toBitsFormat, formatBitsString)
print("... in bytes", toBytesFormat, formatBytesString)
print("... to megabytes",toMBFormat, formatMBString)
print("... to gigabytes", toGBFormat, formatGBString)


