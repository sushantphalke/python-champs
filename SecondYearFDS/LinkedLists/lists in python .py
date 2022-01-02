list0 = []  # here i created empty list
list1 = [1, 2, 3, 4, 5, 6]  # above is list of integers
list2 = [1, 'hello', 'sushant', 3.4]  # 'this is list of mixed data types'
list3 = ["mouse", [8, 4, 6], ['a']]  # list can have another list as an item called nested list
# we can use index operator [] to access item in list
# index is starts with 0
# PRO TIP :NESTED LISTS ARE ACCESSED WITH NESTED INDEXING
my_list = ['s', 'u', 's', 'h', 'a', 'n', 't']
print(my_list[0])  # 's'
print(my_list[5])  # 'n'
print(my_list[-5])  # 's'
print(my_list[-6])  # 'u'
print(my_list[:])  # this prints whole list =['s', 'u', 's', 'h', 'a', 'n', 't']
print(my_list[2:7])  # ['s', 'h', 'a', 'n', 't']
print(my_list[-5:-1])  # ['s', 'h', 'a', 'n']
my_list[0] = 'S'  # changing elements in list
print(my_list)  # ['S', 'u', 's', 'h', 'a', 'n', 't']
my_list[1:4] = ['U', 'S', 'H']
print(my_list)  # ['S', 'U', 'S', 'H', 'a', 'n', 't'] , 2nd to 4th elements had been changed
my_list[4:7] = ['A', 'N', 'T']
print(my_list)  # ['S', 'U', 'S', 'H', 'A', 'N', 'T']
my_list.append('P')
print(my_list)  # ['S', 'U', 'S', 'H', 'A', 'N', 'T', 'P']
my_list.extend(['H', 'A', 'L', 'K', 'E'])
print(my_list)  # ['S', 'U', 'S', 'H', 'A', 'N', 'T', 'P', 'H', 'A', 'L', 'K', 'E']
# append and extend add elements at last only
# now merging of lists
mergedlist = my_list + list1
print(mergedlist)  # ['S', 'U', 'S', 'H', 'A', 'N', 'T', 'P', 'H', 'A', 'L', 'K', 'E', 1, 2, 3, 4, 5, 6]
times5list = list1 * 5  # repeating list many times
print(times5list)  # [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]
# we can insert an element at any location
list1.insert(4, 'Ace')
print(list1)  # [1, 2, 3, 4, 'Ace', 5, 6]
list1[2:2] = ['two', 'three']
print(list1)  # [1, 2, 'two', 'three', 3, 4, 'Ace', 5, 6]
list1[2:3] = ['two', 'three']
print(list1)  # [1, 2, 'two', 'three', 'three', 3, 4, 'Ace', 5, 6]
# what happen to above list why only three repeated not two !!shifted Query !!
list1 = [1, 2, 3, 4, 5, 6]
list1[2] = ['two', 'three']
print(list1)  # [1, 2, ['two', 'three'], 4, 5, 6]
# above list is list in list called nested lists
'''and while we use list[index] =g(without slice operator ) then index element got replaced by 
 given value i.e.=g !! shiftedAns =when we give index[2:2] it started at 2 and ended at 2 so apace
  created to replace when we give index [2:3] then 3-2=1 space generated and this is
   replaced by [two ,three] so firstly stored two got replace by this !IPA!! '''
list1.remove(2)
print(list1)  # [1, ['two', 'three'], 4, 5, 6]
# remove uses element
list1.pop(2)
print(list1)  # pop uses index
del list1[1:3]
print(list1)  # [1, 6]
# del uses index and no index delete entire list
del list1
# print(list1)  # it will gives an error #hence list deleted
list1 = [1, ['two', 'three'], 4, 5, 6]
list1.clear()
print(list1)  # clear() clears all elements
list1 = [1, ['two', 'three'], 5, 6, 7, 9, 4, 5, 6]
list1.index(5)
print(list1)  #
list1.pop(1)
print(list1)  # ['two', 'three']
list1.sort()
print(list1)  # [1, 4, 5, 5, 6, 6, 7, 9]
list1.reverse()
print(list1)  # [9, 7, 6, 6, 5, 5, 4, 1]
print(list1.copy())  # it gives copy only #binkami function [9, 7, 6, 6, 5, 5, 4, 1]
print(list1.count(5))  # count() counts how many times element occur
# lists can be created using functions ,sets,etc.
sqofnumbers = [x ** 2 for x in range(10)]
print(sqofnumbers)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
powersof2 = [2 ** x for x in range(1, 10) if x > 3]
print(powersof2)  # [16, 32, 64, 128, 256, 512]
oddnos = [x for x in range(20) if x % 2 == 1]
print(oddnos)  # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
p = [x + y for x in ['Python ', 'C '] for y in ['Language', 'Programming']]
print(p)  # ['Python Language', 'Python Programming', 'C Language', 'C Programming']
print(25 in sqofnumbers)  # True
print(35 in sqofnumbers)  # False
for intrest in p:
    print(('i like', intrest))
