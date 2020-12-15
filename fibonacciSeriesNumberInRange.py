#Write the python program to find the fibonacci series in the given range.

#Solution:
low = int(input("Enter the lower range:"))
high = int(input("Enter the upper range:"))
def fibonacci(lower, upper):
    container = []
    a = 0
    b = 1
    c = 1
    #
    while a <= upper:
        if a >= lower:
            container.append(a) # 0 1 1
        a = b
        b = c
        c = a+b
    return container


print("The fibonacci series in the given range is :", fibonacci(low,high))

'''Output:
Enter the lower range:5
Enter the upper range:20
The fibonacci series in the given range is : [5, 8, 13]

Process finished with exit code 0'''

