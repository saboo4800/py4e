#Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
#Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours.
#use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
#You should use input to read a string and float() to convert the string to a number.
#Do not worry about error checking the user input - assume the user types numbers properly.

hours = input('how many hours did you work?')

try:
    fhours = float(hours)
except:
    print("please input a number")
    quit()
rate = input("what's your rate?")
try:
    frate = float(rate)
except:
    print("please input a number")
    quit()

standardrate = 40 * frate
totalpay = 0
if fhours > 40:
    extrapay = (fhours - 40) * (1.5 * frate)
    totalpay = extrapay + standardrate
    print(totalpay)
else:
    totalpay = fhours * frate
    print(totalpay)
