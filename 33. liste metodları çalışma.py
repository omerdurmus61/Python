names =['Ali','Yağmur','Hakan','Deniz']
years = [1998,2000,1998,1987]

# 1 Cenk ismini listenin sonuna ekleyin
names.append("Cenk")
#2 Sena ismini listenin başına ekleyin
names.insert(0,"Sena")
#3 Deniz ismini listeden siliniz.
names.remove("Deniz")
#4 Deniz isminin indeksi nedir

#5 Ali ismi listede var mı
a = "Ali" in names
#6 liste elemanlarını ters çevirin
names.reverse()
#7 liste elemanlarını alfabetik olarak sıralayın
names.sort()
#8 years listesini rakamsal büyüklüğe göre sıralayın
years.sort()
#9 str = "Chevrolet,Dacia" karakter dizisini listeye çeviriniz
str ="Chevrolet,Dacia"
result = str.split(",")
print(result)
#10 years listesinin en büyük ve en küçük elemanı nedir.
years.sort()
print(years[0])
print(years[len(years)-1])
min = min(years)
max = max(years)
print(min)
print(max)
#11 years listesinde kaç tane 1998 vardır
a=years.count(1998)
print(a)
#12 years listesinin tüm elemanlarını silniz
years.clear()
print(names)
print(years)
print(str)
print(a)


markalar= []
x=0

while x<3:
    marka = input("marka: ")
    markalar.append(marka)
    x+=1

print(markalar)
