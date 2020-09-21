my_list=list(range(0,11))

def divide (number):
    return number/2

for number in my_list:
    print(divide(number))


def control_string(string):
    if "mekatronik" in string:
        return True

print(control_string("mekatronik mühendisliği"))


def control_string2(string):
        return "mekatronik" in string

print(control_string2("mekatronik mühendisliği"))

#map 

my_job_list=["mekatronik","bilgisayar","makina","elektrik","mekatronik2"]

a=list(map(control_string2,my_job_list))

print(a)

#filter

b=list(filter(control_string2,my_job_list))

print(b)

my_list2=[3,5,7,9]
print( list(map(lambda number:number*4,my_list2)) )
