# Python program for implementation of Radix Sort

import array as array


# A function to do counting sort of ary[] according to
# the digit represented by exp.

def countingSort(arr, exp1):
    n = len(arr)

    # The output array elements that will have sorted ary
    output = [0] * n

    # initialize count array as 0
    count = [0] * 10

    # Store count of occurrences in count[]
    for i in range(0, n):
        index = (arr[i] / exp1)
        count[int(index % 10)] += 1

    # Change count[i] so that count[i] now contains actual
    #  position of this digit in output array
    for i in range(1, 10):
        count[i] += count[i - 1]

        # Build the output array
    i = n - 1
    while i >= 0:
        index = (arr[i] / exp1)
        output[count[int(index % 10)] - 1] = arr[i]
        count[int(index % 10)] -= 1
        i -= 1

    # Copying the output array to ary[],
    # so that ary now contains sorted numbers
    for i in range(0, len(arr)):
        arr[i] = output[i]

    # Method to do Radix Sort


def radixSort(arr):
    # Find the maximum number to know number of digits
    max1 = max(arr)

    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while max1 / exp > 0:
        countingSort(arr, exp)
        exp *= 10


# Driver code to test above

inn = int(input("\nenter the size of array to  test radix sort i.e. n: "))
ary = array.array("i", [])
print(ary)
print("enter the elements of an array ary : ")
for j in range(0, inn):
    a = int(input())
    ary.append(a)
print("new  user  array to  test radix sort is created as : ", ary)

radixSort(ary)
print("new sorted user  array by radix sort as : ", ary)
