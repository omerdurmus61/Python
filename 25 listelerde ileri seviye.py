new_list=[]
new_list2=[]
my_string="barabar"

for element in my_string:
    new_list.append(element)
print(new_list)

new_list2=[element for element in my_string]

print(new_list2)

new_list3=[]

new_list3=[number**5 for number in list(range(0,10))]

print(new_list3)
