numbers  =[1,3,5,9]

#def square (number):
#    return number**2

square = lambda num: num ** 2

#MAP

result = list( map(square,numbers) )
print(result)


for item in map(square,numbers):
    print(item)


#LAMDA

for item in map(lambda num: num ** 2 ,numbers):
    print(item)
