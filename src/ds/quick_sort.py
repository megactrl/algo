def quicksort(arr):
    less = []
    pivotList = []
    more = []

    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        for i in arr:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)
        less = quicksort(less)
        more = quicksort(more)
        return less + pivotList + more


def main():
    arr = [6, 5, 4, 3, 2, 1]
    print('Sorted element using Quicksort: {}'.format(
              ' '.join(map(str, quicksort(arr)))))


if __name__ == '__main__':
    main()
