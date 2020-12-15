#Python program to display the palindrone numbers in the given range.

#Solution:

low = int(input("Enter the lower range number:"))
high = int(input("Enter the upper range number:"))

def print_palindrone(low,high):
    container = []
    for number in range(low,high):
        temp = number
        reverse = 0
        while temp > 0:
            remainder = temp%10
            reverse = reverse *10 +remainder
            temp = temp//10

        if reverse == number:
            container.append(number)

    return container

result = print_palindrone(low,high)
print("The palindrone numbers in the given range are as follows:")
print(result)

'''Output:
Enter the lower range number:100
Enter the upper range number:500
The palindrone numbers in the given range are as follows:
[101, 111, 121, 131, 141, 151, 161, 171, 181, 191, 202, 212, 222, 232, 242,
 252, 262, 272, 282, 292, 303, 313, 323, 333, 343, 353, 363, 373, 383, 393, 404, 414, 424, 434, 444, 454, 464, 474, 484, 494]

Process finished with exit code 0'''