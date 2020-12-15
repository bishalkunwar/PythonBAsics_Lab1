#16.	Program to take a input as string and check the string is on the upper case or in lower case
# if upper case then display is in exact case and then convert string from upper case to lower case
# and vice versa.

#Solution:

take = input("Enter any word/String: ")

def caseCalculator(word):
    values = []

    result = ''
    case = ''

    if word == word.upper():
        word = word.lower()
        case = "uppercase"
        result = "converted to lowercase"
    elif word == word.lower():
        word = word.upper()
        case = "lowercase"
        result = "converted to uppercase"
    else:
        case = "not any case"
        result = "same"

    values.append(word)
    values.append(case)
    values.append(result)

    return values

    # Checking condition for displaying result


if caseCalculator(take)[1] == "same":
    print("The given string {0} is now being printed as the same string {1}"
          "as it doesnt satisfy the given condition.".format(take, take))
else:
    print("The given string {0} which was {1} is now {2} as {3}.".format(take,caseCalculator(take)[1], caseCalculator(take)[2],caseCalculator(take)[0]))



#Output

'''Enter any word/String: helloworld
The given string helloworld which was lowercase is now converted to uppercase as HELLOWORLD.

Process finished with exit code 0
'''