import array as arr

# ***************LINEAR _ SEARCHING ****************************

# this is linear searching in array by traversing each element irrespective of it found or not each
# element is checked compulsory.
# if we want to know only first found element info then add break statement in a function while loop.
# algo of linear search

def linearsearch():
    key = int(input("enter the element to linear search in numbers : "))
    for i in range(0, n):
        if p[i] == key:
            print(key, "  is at index : ", i)


# *************** BINARY _ SEARCHING _ function ****************************

# calling binary search function created above

def binarysearch():
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


n = int(input("\nenter the size of array to test searching methods in array i.e. n : "))
p = arr.array("i", [])
print(p)
print("enter the elements of an array p : ")
for x in range(0, n):
    a = int(input())
    p.append(a)
print("new  user  array to  test searching methods is created as : ", p)

linearsearch()
binarysearch()
