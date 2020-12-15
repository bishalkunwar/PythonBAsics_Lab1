#Python program to find the factorial of given number

#Solution

number = int(input("Enter the number to find the factorial:"))

def factorials(num):
    factorial = 1
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        while num > 0:
            factorial = factorial * num
            num = num-1
        return factorial

print("The factorial of ",number,"is ",factorials(number))

'''Output:
Enter the number to find the factorial:5
The factorial of  5 is  120

Process finished with exit code 0
'''