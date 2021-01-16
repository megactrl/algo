def binary_search(the_list , item):
    first = 0
    last = len(the_list)-1
    found = False

    while first <= last and not found:
        mid = (first + last)// 2

        if the_list[mid] == item:
            found=True

        else:
            if item < the_list[mid]:
                last = mid - 1

            else:
                first = mid + 1

    return found
the_list = [10, 12, 13, 14, 15, 16, 17, 18, 19]
item = 19

if binary_search(the_list,item):
    print("The item is in the list")

else:
    print("The item is not in the list")

