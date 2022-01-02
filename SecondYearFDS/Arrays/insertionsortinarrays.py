import array as arr

#  *************** INSERTION _ SORTING ***************************
def insertionsort():

    for i in range(1, n):
        current = p[i]
        j = i - 1
        while p[j] > current and j >= 0:
            p[j + 1] = p[j]
            j = j - 1
        p[j + 1] = current
    print("\nsorted array by insertion sort : ", p)


n = int(input("\nenter the size of array to  test INSERTION sort i.e. n : "))
p = arr.array("i", [])
print(p)
print("enter the elements of an array p : ")
for x in range(0, n):
    a = int(input())
    p.append(a)
print("new  user p array to  test INSERTION sort is created as : ", p)

insertionsort()
