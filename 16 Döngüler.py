#For & while

my_list=[1,2,3,4,5]

for number in my_list:
    print("Döngü",number)

print("----------")

for number in my_list:
    number=number*5
    print(number)

print("----------")

for number in my_list:
    if number%2==0:
        print(number)

print("----------")

my_string="Mustafa Kemal Atatürk"

for letter in my_string:
    print(letter)

print("----------")

my_new_set={("a","b"),("c","d"),("e","f"),("g","h")}
for element in my_new_set:
    print(element)


print("-"*10,"Örnek 1'nin çıktısı","-"*10)

for (x,y) in my_new_set:
    print(x)

print("-"*10,"Örnek 2'nin çıktısı","-"*10)

for (x,y) in my_new_set:
    print("[x]'in değeri:",x,"[y]'nin değeri:",y)

    my_tuple_list=[(0,1,2),(2,3,4),(9,10,11)]
       
for (x,y,z) in my_tuple_list:
    print(z)

   

   
