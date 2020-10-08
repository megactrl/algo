# Heap Sort


def heap(arr, n, i):
      largest = i
      l = 2 * i + 1
      r = 2 * i + 2

      if l < n and arr[i] < arr[l]:
          largest = l

      if r < n and arr[largest] < arr[r]:
          largest = r

      if largest != i:
          arr[i], arr[largest] = arr[largest], arr[i]
          heap(arr, n, largest)


def heapSort(arr):
      n = len(arr)

      for i in range(n//2, -1, -1):
          heap(arr, n, i)

      for i in range(n-1, 0, -1):
          # Swap
          arr[i], arr[0] = arr[0], arr[i]

          # Heap root element
          heap(arr, i, 0)


arr = [1, 43, 12, 25, 46, 33, 60, 10]
heapSort(arr)
n = len(arr)
print("Sorted array is")
for i in range(n):
    print("%d " % arr[i], end='')


#time complexities O(nlogn)
