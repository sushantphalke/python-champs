import array as arr
# **************** QUICK  _ SORTING ***************************

# The main function that implements QuickSort
# ary[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index

def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Function to do Quick sort

def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        # pi is partitioning index, ary[p] is now
        # at right place
        par = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, par - 1)
        quickSort(arr, par + 1, high)


#  Driver code to test above

n = int(input("\nenter the size of array to  test quick sort i.e. n : "))
p = arr.array("i", [])
print(arr)
print("enter the elements of an array p : ")
for x in range(0, n):
    a = int(input())
    p.append(a)

print("new  user  array to  test quick sort is created as : ", p)
quickSort(p, 0, n - 1)
print("Sorted array by quick sort is:", p)

# $ PRO TIP: QUICK SORT IS QUICK METHOD FOR SORTING. IN FACT IT IS LENGTHY IN ALL METHODS TO CODE BUT EFFECTIVE IN TIME
