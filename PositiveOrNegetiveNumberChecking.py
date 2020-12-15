#Write a python program to check if the given number is positive or negetive.

#Solution

def check(num):
    if num > 0:
        print(num, " is the positive number.")
    elif num == 0:
        print(num," is equals to zero.")
    else:
        print(num, " is the negetive number.")

check(-1)
check(1)
check(0)
num = int(input ("Enter the input number to check:"))
check(num)

'''Output:
-1  is the negetive number.
1  is the positive number.
0  is equals to zero.
Enter the input number to check:15
15  is the positive number.

Process finished with exit code 0'''