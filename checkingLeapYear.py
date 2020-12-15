# python program to check the user input is a leap year or not?

#Solution:

year = int(input("Enter the year to check leap year: "))

def year_check(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                print("{0} is a leap year".format(year))
            else:
                print("{0} is not a leap year".format(year))
        else:
            print("{0} is a leap year".format(year))
    else:
        print("{0} is not a leap year".format(year))

year_check(year)

#Output:

'''Enter the year to check leap year: 2000
2000 is a leap year

Process finished with exit code 0
'''

'''Enter the year to check leap year: 2017
2017 is not a leap year

Process finished with exit code 0'''