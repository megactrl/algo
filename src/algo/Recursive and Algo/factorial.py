# Recursive Function for calculating factorial of a number

def fact(num):
    print(" Function called with num = " + str(num))
    if num == 1:
        return 1
    else:
        ans = num * fact(num - 1)
        print("Intermediate result for", num, "* fact(" ,num - 1, ") :", ans)
        return ans

print("Factorial = :", fact(5))
