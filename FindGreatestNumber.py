#Write the python program to find the greatest number among the three numbers.

#Solution:
def greatest(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num3 and num2 >= num1:
        return num2
    else:
        return num3


num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
num3 = int(input("Enter the third number:"))

largest = greatest(num1, num2, num3)
print(largest,"is the largest number among the given input numbers.")

'''Output:
Enter the first number:20
Enter the second number:10
Enter the third number:15
20 is the largest number among the given input numbers.

Process finished with exit code 0'''