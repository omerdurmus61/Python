#Tuple

my_tuple=[1,2,3,1,1,1,"a","b"]

my_tuple=tuple(my_tuple)

print(my_tuple)

#my_tuple[0]=61 Tuple içindeki veriler değişemez.

print( my_tuple.count(1) )

print( my_tuple.index("a") )

#1 elemanının indexini verirken ilk gözüktüğü yeri verir yani 0.indis.
print( my_tuple.index(1) )