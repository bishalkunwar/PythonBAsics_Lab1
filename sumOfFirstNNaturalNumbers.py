#Python program to find the sum of first n natural numbers:

#Solution:

number = int(input("Enter the number to find the sum upto: "))

def calculator(number):
    sum = 0
    while (number > 0):
        sum = sum + number
        number = number - 1
    return sum

#calculator(number)
def display():
    result = calculator(number)
    print("The sum of natural number upto ",number,"is: ",result)
display()

#Output:
'''Enter the number to find the sum upto: 10
The sum of natural number upto  10 is:  55

Process finished with exit code 0'''