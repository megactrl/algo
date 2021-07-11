# Calculate the sum of a list of number like [3,4,5,7,8,9,12] without recursion 

def calsum(List):
    sum = 0
    for flag in List:
        sum = sum + flag
    return sum

List = [3,4,5,7,8,9,12]
print(" Given List is :", List)
print("SUm of List of numbers is : ", calsum(List))

# Source code with recursion

def sumList(myList):
    if len(myList) == 1:
        return myList[0]

    else:
        return myList[0] + sumList(myList[1:])

myList = [3,4,5,6,8,9,2]
print("The given list is :",myList)
print("Sum of the list of numbers : ", sumList(myList))