#Python program to check if the number is palindrone or not.

#Solution:

inp = input("Enter the number to check:")

def check_palindrone(str):
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
        return True

result = check_palindrone(inp)
if (result):
    print("Yes,",inp,"is palindrone.")
else:
    print("No,",inp,"is not palindrone.")


'''Output:
Enter the number to check:12321
Yes, 12321 is palindrone.

Process finished with exit code 0
'''