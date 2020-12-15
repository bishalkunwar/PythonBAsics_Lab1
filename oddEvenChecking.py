#Python program to check if the input number is odd or even.

#Solution:

number = int(input("Enter the input number to check:"))

def checker(number):
    if number % 2 == 0:
        return True
    return False

result = checker(number)
if (result):
    print(number,"is an even number.")
else:
    print(number,"is an odd number.")

'''Output:
Enter the input number to check:24
24 is an even number.

Process finished with exit code 0
'''