from random import *

sayi = randint(1,100)

bildiMi = 0

while (bildiMi == 0):
    
    tahmin = int (input("Bir sayi giriniz(1-100):"))

    if tahmin < sayi :
        print("yukarı")

    elif tahmin > sayi :
        print("aşağı")
    else :
        print("Bildiniz.")
        bildiMi = 1