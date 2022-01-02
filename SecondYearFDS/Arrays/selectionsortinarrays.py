import array as arr


# ***************SELECTION _ SORTING****************************

#  in this method elements are compare with one another and array get sorted.
def selectionsort():
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if p[j] < p[i]:
                temp = p[j]
                p[j] = p[i]
                p[i] = temp
    print("\nsorted array by selection sort : ", p)


n = int(input("\nenter the size of array to  test selection sort i.e. n : "))
p = arr.array("i", [])
print(p)
print("enter the elements of an array p : ")
for x in range(0, n):
    a = int(input())
    p.append(a)
print("new  user pi array to  test selection sort is created as : ", p)
selectionsort()
