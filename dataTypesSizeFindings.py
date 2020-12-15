#python program to find the size of datatypes:

#Solution:

import sys

choice = int(input("Enter the choice:\n1:for int.\n2:for float\n3:for double\n4:for char\nelse:exit"))

if choice == 1:
    print("The size of int is",sys.getsizeof(int()))
elif choice == 2:
    print("The size of float is", sys.getsizeof(float()))
elif choice == 3 or choice == 4:
    print("This has no datatypes in python")
else:
    exit()

'''output:
sir, i got error on this program on how to use the library

Enter the choice:
1:for int.
2:for float
3:for double
4:for char
else:exit1
The size of int is 24

Process finished with exit code 0'''
