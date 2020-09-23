numbers = [1,2,3,4,5,6,7,12,45,26,22]
letters = ["a","b","c"]
#listenin sonuna belirilen elemanı ekler.
letters.append("omer")
letters.append("can")
letters.append("durmus")
#belirtilen indise o oelemanı ekler
numbers.insert(3,16)
numbers.insert(-1,16)
#en ve ya belirtilen elemanı siler sondaki elemanı siler
numbers.pop()
numbers.pop(0)
numbers.pop(3)
# belirtilen elemanı siler
letters.remove("can")
numbers.remove(45)
#sıralama yapar
numbers.sort()
letters.sort()
#ters çevirir
numbers.reverse()
letters.reverse()
#belirtilen elemanı sayar
print(numbers.count(3))
print(letters.count("omer"))
#elemanları siler
numbers.clear()



print(numbers)
print(letters)