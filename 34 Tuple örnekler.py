#tuple tipi liste ile aynıdır sadece değişmezlik özelliği vardır ekleme çıkarma yapamayız.
my_list = [1,2,3,4]
my_tuple = ("ahmet","ayşe","özgür","ensar","ensar")

my_list[0]=16
print(my_list)
#tuple veri tipinde değişmezlik özelliği vardır.
#tuple[0]=61

print( my_tuple.index("ensar") )

print( my_tuple.count("ensar") )

my_tuple2 = (1,2,3) + my_tuple

print(my_tuple2)