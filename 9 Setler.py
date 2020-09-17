#setler
#set veri tipinde aynı elemanda birden fazla olamaz.
my_list=[1,1,2,2,3,3]
print(my_list)
print(type(my_list))
#sete'e çevirme işlemi
my_list=set(my_list)

print(my_list)
print(type(my_list))

my_set={1,2,3,1}
print(my_set)

my_set1={"a","b","a"}
print(my_set1)

#Listeleri ya da setleri boş bırakma

my_list1=[]
print(my_list1)

#Bir seti boş bıraktığımızda

my_new_set={}
print(my_new_set)

#Boş bırakmak istediğimiz setin veri tipini dic yani dictionary olarak algıladı ikisinde de {} kullanıldığı için.

my_new_set =set()
print(my_new_set)

my_new_set.add(1)
my_new_set.add(2)
my_new_set.add(3)
print(my_new_set)


my_dictionary=dict()

print(my_dictionary)

my_dictionary["key1"]=1

print(my_dictionary)

my_list2=[]
print(type(my_list2))

my_list2.append(1)
my_list2.append(2)
my_list2.append([1,"a"])

print(my_list2)