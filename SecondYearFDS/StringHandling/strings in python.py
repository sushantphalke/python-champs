my_string = 'hello'
print(my_string)  # hello
my_string = "hello"
print(my_string)  # hello
my_string = '''hello'''
print(my_string)  # hello
# three types of coats to give string character
my_string = '''hello welcome to another world '''
print(my_string)  # hello welcome to another world
my_string1 = 'programming'
print('str=', my_string1)  # str= programming
print(my_string1[0])  # 'p'
print(my_string1[1])  # 'r'
print(my_string1[3])  # 'g'
print(my_string1[-1])  # 'g'
print(my_string1[-3])  # 'i'
print(my_string1[1:5])  # 'rog'
print(my_string1[3:-2])  # 'grammi'
# If we try to access an index out of the range or use numbers other than an integer, we will get errors.
my_string = 'programming'
del my_string
# print (my_string)  # then  we will got an error hence successfully deleted the  string
string1 = 'welcome to '
string2 = 'Ace world'
print(string1 + string2)  # welcome to Ace world
print(string1 * 5)  # 'welcome to welcome to welcome to welcome to welcome to '
print((string1+string2)*5)
# welcome to  Ace world  welcome to Ace world welcome to Ace world welcome to Ace world welcome to Ace world'
count = 0
for letter in 'welcome to Ace world':
    if letter == 'o':
        count += 1
print(count, 'letters o found')
print('a' in 'Godzilla')  # true # it checks the for availability of string in given string
print('b' in 'Godzilla')  # false # it checks the for availability of string in given string
print('bro' in 'brother')  # true # it checks the for availability of string in given string
# now how to take string as input
password = input('input your password  ')
if 'sushant' == password:
    print(' Login passed')
else:
    print('login failed')
