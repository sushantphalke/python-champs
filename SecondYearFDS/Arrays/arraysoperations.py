import array as arr

s = arr.array('i', [12, 13, 14, 15, 19, 78, 6, 756, 45, 34])
u = arr.array('d', [23.24, 33.34, 43.44, 54.55])

print("\n**************  OPERATIONS ON ARRAY  **********************\n")

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print("numbers list = ", numbers)
numbers_array = arr.array('i', numbers)
print("this new numbers array by taking whole list into it", numbers_array)
#   here we had added numbers list to make integer number array
print('numbers array from 2nd index to 5th no. : ', numbers_array[2:5])
print('number at up to -5th index', numbers_array[:-5])
print('number at from 5th index', numbers_array[5:])
print('number at -5th index', numbers_array[-5])
print('number at all indexes', numbers_array[:])

numbers_array[0] = 0
numbers_array[-5] = 34

print("numbers at 0th and -5th has ben changed array is : ", numbers_array)
numbers_array[3:7] = arr.array('i', [11, 12, 13, 14, 15])
print("updated numbers array : ", numbers_array)
numbers_array.append(100)
print("updated numbers array : ", numbers_array)
numbers_array.extend([200, 300, 400])
print("updated numbers array : ", numbers_array)

x = arr.array('i', [111, 222, 333, 444, 555])
y = arr.array('i', [666, 777, 888, 999])
# sumxy = ary.array('i')  # this an empty array
sumxy = x + y
print("addition of two arrays sumxy : ", sumxy)
sumxy.remove(333)  # remove uses element
sumxy.pop(4)  # pop uses index
print("updated sumxy : ", sumxy)
del sumxy  # sumxy array will be deleted

'''1)If you create arrays using the array module,all elements of the array must be of the same numeric type. 2) lists 
can have string arrays doesn't and at every time of assigning array elements type must be defined as it is integer or 
float or something else 

   PRO  TIP :
   WHEN TO  USE ARRAYS :
   $- LISTS ARE MORE FLEXIBLE THAN ARRAYS THEY CAN STORE ELEMENTS OF DIFFERENT DATA TYPES ALSO STRINGS TOO.
  $$- IF YOU HAVE TO DO MUCH MATHEMATICAL WORK YOU MAY GO WITH NUMPY LIB.
'''

#  ****************** CREATING AN USER DEFINED ARRAY **************************

#  this is user defined array

n = int(input("\nenter the size of array to  test linear search i.e. n : "))
p = arr.array("i", [])
print(p)
print("enter the elements of an array : ")
for i in range(0, n):
    a = int(input())
    p.append(a)

print("p array is created as : ", p)
#
#
#
#
#
#
#
#
#
#
#
print("\n**************  SEARCHING IN ARRAY  **********************\n")
"""
# ***************LINEAR _ SEARCHING ****************************

# this is linear searching in array by traversing each element irrespective of it found or not each
# element is checked compulsory.
# if we want to know only first found element info then add break statement in a function while loop.
# algo of linear search

key = int(input("enter the element to linear search in numbers : "))
for i in range(0, n):
    if p[i] == key:
        print(key, "  is at index : ", i)

# *************** BINARY _ SEARCHING _ function ****************************

# calling binary search function created above

binarykey = int(input("enter the element to binary search in array i.e. binarykey -: "))
h = 0
e = n
while h <= e:
    mid = (h + e) // 2
    if p[mid] == binarykey:
        print(binarykey, " is at index : ", mid)
        break
    elif p[mid] > int(binarykey):
        e = mid - 1
    else:
        h = mid + 1

# ****************************SORTING IN AN ARRAY ****************************

# ***************SELECTION _ SORTING****************************

#  in this method elements are compare with one another and array get sorted.

for i in range(0, n - 1):
    for j in range(i + 1, n):
        if p[j] < p[i]:
            temp = p[j]
            p[j] = p[i]
            p[i] = temp

print("\nsorted array by selection sort : ", p)

#  *************** BUBBLE _ SORTING ****************************

# in this method adjacent elements are compare with one another and array get sorted.
# ********** CREATING AN ARRAY ********
ni = int(input("\nenter the size of array to  test bubble sort i.e. ni : "))
pi = ary.array("i", [])
print(pi)
print("enter the elements of an array pi : ")
for i in range(0, ni):
    ai = int(input())
    pi.append(ai)
# main algo for bubble sort
print("new  user pi array to  test bubble sort is created as : ", pi)
counter = 1
while counter < ni:
    for i in range(0, ni - counter):
        if pi[i] > pi[i + 1]:
            temp = pi[i]
            pi[i] = pi[i + 1]
            pi[i + 1] = temp
    counter = counter + 1
print("\nsorted array by bubble sort : ", pi)

#  *************** INSERTION _ SORTING ***************************

nii = int(input("\nenter the size of array to  test INSERTION sort i.e. nii : "))
pii = ary.array("i", [])
print(pii)
print("enter the elements of an array pii : ")
for i in range(0, nii):
    aii = int(input())
    pii.append(aii)

print("new  user pi array to  test INSERTION sort is created as : ", pii)
# main algo for insertion sort
for i in range(1, nii):
    current = pii[i]
    j = i - 1
    while pii[j] > current and j >= 0:
        pii[j + 1] = pii[j]
        j = j - 1
    pii[j + 1] = current
print("\nsorted array by insertion sort : ", pii)


#  **************** QUICK  _ SORTING ***************************

# The main function that implements QuickSort
# arrr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index

def partition(arrr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arrr[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if arrr[j] <= pivot:
            # increment index of smaller element
            i = i + 1
            arrr[i], arrr[j] = arrr[j], arrr[i]

    arrr[i + 1], arrr[high] = arrr[high], arrr[i + 1]
    return (i + 1)


# Function to do Quick sort

def quickSort(arrr, low, high):
    if len(arrr) == 1:
        return arrr
    if low < high:
        # pi is partitioning index, ary[p] is now
        # at right place
        par = partition(arrr, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arrr, low, par - 1)
        quickSort(arrr, par + 1, high)


#  Driver code to test above

niii = int(input("\nenter the size of array to  test quick sort i.e. niii : "))
arrr = ary.array("i", [])
print(arrr)
print("enter the elements of an array arrr : ")
for i in range(0, niii):
    aiii = int(input())
    arrr.append(aiii)

print("new  user pi array to  test quick sort is created as : ", arrr)
niii = len(arrr)
quickSort(arrr, 0, niii - 1)
print("Sorted array by quick sort is:", arrr)

# $ PRO TIP: QUICK SORT IS QUICK METHOD FOR SORTING. IN FACT IT IS LENGTHY IN ALL METHODS TO CODE BUT EFFECTIVE IN TIME

#  ****************  MERGE _ SORTING ***************************
# Python program for implementation of MergeSort
# Merges two subarrays of ary[].
# First subarray is ary[l..m]
# Second subarray is ary[m+1..r]
def merge(ary, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = ary[l + i]

    for j in range(0, n2):
        R[j] = ary[m + 1 + j]

        # Merge the temp arrays back into ary[l..r]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = l  # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            ary[k] = L[i]
            i += 1
        else:
            ary[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        ary[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        ary[k] = R[j]
        j += 1
        k += 1


# l is for left index and r is right index of the
# sub-array of ary to be sorted
def mergeSort(ary, l, r):
    if l < r:
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = (l + (r - 1)) // 2

        # Sort first and second halves
        mergeSort(ary, l, m)
        mergeSort(ary, m + 1, r)
        merge(ary, l, m, r)

    # Driver code to test above


niiii = int(input("\nenter the size of array to  test merge sort i.e. niiii : "))
arrry = ary.array("i", [])
print(arrry)
print("enter the elements of an array arrry : ")
for i in range(0, niiii):
    aiii = int(input())
    arrry.append(aiii)

print("new  user pi array to  test merge sort is created as : ", arrry)
mergeSort(arrry, 0, niiii - 1)
print("\nSorted array is", arrry)

#  ****************  RADIX _ SORTING ***************************
# Python program for implementation of Radix Sort

# A function to do counting sort of ary[] according to
# the digit represented by exp.
def countingSort(ary, exp1):
    n = len(ary)

    # The output array elements that will have sorted ary
    output = [0] * (n)

    # initialize count array as 0
    count = [0] * (10)

    # Store count of occurrences in count[]
    for i in range(0, n):
        index = (ary[i] / exp1)
        count[int((index) % 10)] += 1

    # Change count[i] so that count[i] now contains actual
    #  position of this digit in output array
    for i in range(1, 10):
        count[i] += count[i - 1]

        # Build the output array
    i = n - 1
    while i >= 0:
        index = (ary[i] / exp1)
        output[count[int((index) % 10)] - 1] = ary[i]
        count[int((index) % 10)] -= 1
        i -= 1

    # Copying the output array to ary[],
    # so that ary now contains sorted numbers
    i = 0
    for i in range(0, len(ary)):
        ary[i] = output[i]

    # Method to do Radix Sort


def radixSort(ary):
    # Find the maximum number to know number of digits
    max1 = max(ary)

    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while max1 / exp > 0:
        countingSort(ary, exp)
        exp *= 10


# Driver code to test above


for i in range(len(ary)):
    print(ary[i]),
niiiii = int(input("\nenter the size of array to  test radix sort i.e. niiiii : "))
arrryy = ary.array("i", [])
print(arrryy)
print("enter the elements of an array arrryy : ")
for i in range(0, niiiii):
    aiii = int(input())
    arrryy.append(aiii)

radixSort(arrryy)
print("new  user pi array to  test radix sort is created as : ", arrryy)
"""