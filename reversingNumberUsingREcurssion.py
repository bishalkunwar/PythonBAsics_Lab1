# Write a python program to reverse the given input number using recurssion

#Solution

inp = input("Enter the number to reverse that:")

def reverse(num):
    if num[0] == '-':
        num = int('-' + num[-1:0:-1])
        return num
    num = int(num)
    reverse_num = 0
    while num > 0:
        remainder = num % 10
        reverse_num = (reverse_num * 10) + remainder
        num = num // 10
    return reverse_num


reversed_num = reverse(inp)
print("The reversed number is:",reversed_num)

'''Output:
Enter the number to reverse that:154
The reversed number is: 451

Process finished with exit code 0'''