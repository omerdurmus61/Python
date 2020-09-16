#Karakter dizilerinde değişmezlik.
#immutability

name="omer can durmus"
print(name[0])

#isim[0]= A hatalı kullanım.

my_list=[1,2,3]

print(my_list)

print(my_list[0])

#Geçerli bir kullanımıdır.
my_list[0]=5

print(my_list[0])


my_list[2]=6

print(my_list[2])

#my_list=my_list.append[7]

print(my_list)
#sondaki elemanı çıkartır.
my_list.pop()

print(my_list)

my_mixed_list=[1,2,"a","abc"]

print(my_mixed_list[0])
print(my_mixed_list[-1])

#listeler ile işlemler.

my_list1=["a","b","c"]
my_list2=["d","e","f"]

my_list3=my_list1+my_list2

print(my_list3)
#çapma işlemi bu listede işe yarar.
print(my_list1*3)

my_list1.reverse()

print(my_list1)


