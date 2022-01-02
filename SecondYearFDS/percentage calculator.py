import string as str
def calculaltePercentage(value1, totalofvalues):
    percentage =((value1 / totalofvalues)*100)
    return percentage


totalofvalues = 4619976274
howmanyvalues= input('enter no of values:')
howmanyvalues= int(howmanyvalues)
for i in range (0,howmanyvalues):
    value1= input('input value')
    value1= int(value1)
    print('percentage')
    print(calculaltePercentage(value1, totalofvalues))

