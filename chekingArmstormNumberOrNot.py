# Python program to check if the given number is armstorm or not.

# Solution:
import math

number = int(input("Enter the input number:"))  # Taking user input.


def check_armstorm(num):  # Defining method to implement the logic
    num = str(num)
    length = len(num)
    num = int(num)
    sum = 0
    temp = num
    while temp > 0:
        remainder = temp % 10
        sum = sum + pow(remainder, length)
        temp = temp // 10
    return sum


result = check_armstorm(number)
if number == result:
    print(number, "is an armstorm number.")
else:
    print(number, "is not an armstorm number.")


'''Output:
Enter the input number:12321
12321 is not an armstorm number.

Process finished with exit code 0'''