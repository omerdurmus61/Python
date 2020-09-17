#STRING

# 1) Aşağıdaki String'in 5. harfini my_letter isimli bir değişkene atayınız.

my_string="James Hetfield"

#cevap 

my_latter = my_string[4]
print(my_latter)

# Aşağıdaki String'in 5. ve 8. karakteri arasındaki tüm harflerini yazdırınız (5 ve 8 dahil)

my_new_string = "QuentinTarantino"

#cevap

print(my_new_string[4:8])

# Aşağıdaki String'i kod ile tersten yazın

my_last_string = "Afyonkarahisarlılaştıramadıklarımızdanmısınız"

#cevap

print(my_last_string[::-1])

#INTAGER & FLOAT

# 1) Aşağıdaki işlemin sonucu hangi veri tipinde olacaktır?

#3 + 10.2 + 50

#cevap

x =3 + 10.2 + 50
print(type(x))#float

# 2) Aşağıdaki işlemin sonucu kaçtır?

#5 + 8 * 12

#cevap

print(5 + 8 * 12)

#LIST & DICTIONARY & SET

# 1) Bu listeyi 3 farklı yoldan oluşturunuz: [1,2,"a"]

# Cevap 1.a)
my_list1=[1,2,"a"]
print(my_list1)
# Cevap 1.b)
my_list2=[]
my_list2.append(1)
my_list2.append(2)
my_list2.append("a")
print(my_list2)
# Cevap 1.c)
my_temp_list1=[1,2]
my_temp_list2=["a"]
my_list3=my_temp_list1+my_temp_list2
print(my_list3)

# 2) Aşağıdaki "a"'yı tek satırda alınız
List = [1,4,[2,3,"a"]]
#cevap
print( List[2][2]  )

# 3) Aşağıdaki "b"'yi tek satırda alınız:

my_dictionary = {"k1":2, "kk":[4,{"kkkk":"b"}]}

print( my_dictionary["kk"][1]["kkkk"]  )

# 4) Aşağıdaki liste set'e çevirilince hangi değerler içinde kalacaktır?

my_list_to_be_set = [11,12,22,33,11,22,45,32,21,22,33,45]

#cevap

my_list_to_be_set= set(my_list_to_be_set)

print(my_list_to_be_set)

# 1) Aşağıdaki ifadenin sonucu ne olacaktır?

x = 40 * 5 + 3

y = 208 - 2 * 4

#x > y
#cevap

print(x>y)#True

# 2) Aşağıdaki ifadenin sonucu ne olacaktır?


a = 40 * (4 - 2)


b = 80 - 2 * -5

#a > b

#cevap

print(a>b)#False
