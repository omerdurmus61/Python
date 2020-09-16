
my_string = "Hello world"

#Dizi indisine göre karakter yazdırma
print("--------------")
#0. indis 1.elemana demektir.
print(my_string[0])
#1.indis 2.eleman demektir
print(my_string[1])
print(my_string[2])
print(my_string[3])
print(my_string[4])
print("--------------")
#Eğer sondan 1.elemanı yani en son indisi çağırmak istiyorsak my_string[-1] deriz.
print(my_string[-1])
#Matematikte -0 şeklinde diye bir kavram olmadığı için sondan eleman çağırmak istersek -1 den başlatız.
print(my_string[-2])
print(my_string[-3])
print(my_string[-4])
print(my_string[-5])

print("--------------")

my_string2="1234567890"
#ilk elemanı verecektir.
print(my_string2[0])
#ilk iki elemandan sonrasını verecektir.
#Bu işleme slicing yani kesme işlemi deniyor.
print(my_string2[2:])
#Aynı işlemi ilk elemanlar için de yapabiliriz.
#ilk iki elemanı verecektir.
print(my_string2[:2])
#Bu mantığa stopping indeks yani durdurma indeksi deniyor .
# Kısaca : neredeyse (sağ ya da sol) oradaki sizin girdiğiniz sayıya kdar olan ya da ondan sonraki diğer elemanları ekrana bastırıyor
print(my_string2[:4])

#Bir diğer kullanım aralık belirtme.
#Bu kullanımda baştan ikinci terimden sonrakileri diyoruz ve ona ek olarak baştan 4.terim ve öncesini istiyoruz.
#Yani 2.terimden sonra 34567890 var biz 4.terim ve öncesini de istiyorduk 34 kalıyor.
print(my_string2[2:4])


print(my_string2[::])
#Hepsini gösterir.
print(my_string2[::2])
#0.karakterden başlar 2'şer sayı atlar ve yazar dizi bitene kadar devam eder.
print(my_string2[2:4:2])
#Bu kullanım 2'den başlar 4'te durur ve 2'şer atlarıp yazdırır.


#son kullanım olarak tersten yazdırma
print(my_string2[::-1])


