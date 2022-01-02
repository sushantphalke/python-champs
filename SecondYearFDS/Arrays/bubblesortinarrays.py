import array as arr


#  *************** BUBBLE _ SORTING ****************************

# in this method adjacent elements are compare with one another and array get sorted.
# main algo for bubble sort

def bubblesort():
    counter = 1
    while counter < n:
        for i in range(0, n - counter):
            if p[i] > p[i + 1]:
                temp = p[i]
                p[i] = p[i + 1]
                p[i + 1] = temp
        counter = counter + 1
    print("\nsorted array by bubble sort : ", p)


# ********** CREATING AN ARRAY ********
n = int(input("\nenter the size of array to  test bubble sort i.e. n : "))
p = arr.array("i", [])
print(p)
print("enter the elements of an array p : ")
for x in range(0, n):
    a = int(input())
    p.append(a)
print("new  user pi array to  test bubble sort is created as : ", p)
bubblesort()