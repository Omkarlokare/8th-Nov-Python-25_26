print("----Leap year----")
#Leap year or not
year = 1900

if year % 4 == 0:
# and year % 100 != 0 or year % 400 == 0):
    print(year, "is a leap year")

else:
    print(year, "is not a leap year")