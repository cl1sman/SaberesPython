"""
    Leap Year Rules: How to Calculate Leap Years

    In our modern-day Gregorian calendar, three criteria must be taken into account to identify leap years:
        * The year must be evenly divisible by 4;
        * If the year can also be evenly divided by 100, it is not a leap year;
	        
            unless...
        * The year is also evenly divisible by 400. Then it is a leap year.

According to these rules, the years 2000 and 2400 are leap years,
while 1800, 1900, 1989, 2100, 2200, 2300, and 2500 are not leap years.
"""
year = int(input("The year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year")
        else:
            print("Not Leap Year")
    else:
        print("Leap Year")
else:
    print("Not Leap Year")