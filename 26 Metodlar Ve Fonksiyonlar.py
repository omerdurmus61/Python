#Metod örneği 
#metodlar sınıflar içersinde kullanılır.

my_string="mekatronik"

my_string= my_string.upper()

print(my_string)

#Fonksiyon örneği fonksiyonlar sınıfların sdışında olur.


def my_mekatronik():
    print("Fonksiyon çalıştı.")

my_mekatronik()


def hello(name = "Python"):
    print("Hello") 
    print(name)

hello()

def topla(number1,number2):
    number3=number1+number2
    print(number3)

topla(3,4)

def summation (n1,n2,n3):
    return n1+n2+n3

my_result =summation(10,20,30)

print(my_result)

def mecatronics(s):
    if s[0]== "m":
       print( s.capitalize())

mecatronics("mekatronik")

def toplam(*args):
    return sum(args)

a= toplam(1,2,3,4,5)
print(a)

def my_func (*argumanlarrrr):
    print(argumanlarrrr)
    
my_func("omer","can","mekatronik","61")

def my_func2(**kwargs):
    print(kwargs)

my_func2(run=100,swim=200,basketball=300)


def my_func3 (**kwargs):
    if "merhaba" in kwargs:
        print("merhaba var")
    else:
        print("merhaba yok")

my_func3 (merhaba=10,naber=20,nasılsın=30)        