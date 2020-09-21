from random import *
"""from random import randint
from random import choice
from random import shuffle"""

zar1=randint(1,6)
zar2=randint(1,6)

if zar1==zar2:
    print(f"zar1:{zar1} zar2:{zar2} tebrikler")
else:
    print(f"zar1:{zar1} zar2:{zar2} tekrar deneyin.")


my_list = ["omer","can","durmus",1,2,3,61]

print(choice(my_list))

my_number_list = list(range(0,10))

my_number_list = shuffle(my_number_list)

print(my_number_list)