#Python program to find the prime numbers in given range.

#Solution

low = int(input("Enter the lower range:"))
high = int(input("Enter the upper range:"))

def primeFinder(low,high):
    container = []
    for number in range(low,high):
        if number >= 1:
           for i in range (2,number):
               if number == 2:
                   container.append(number)
               elif number % i == 0:
                   break
               else:
                   container.append(number)
                   break
    return container

print("The prime numbers in given range are:",primeFinder(low,high))


'''Output:
Enter the lower range:5
Enter the upper range:25
The prime numbers in given range are: [5, 7, 9, 11, 13, 15, 17, 19, 21, 23]

Process finished with exit code 0'''