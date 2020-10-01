#class oyun diss to Özgür Emre Uçar ve Arkadaşı
from random import *


class Karakter():
    can = 100
    def __init__(self,ad):
        self.ad = ad

    def saldır(self):
        
        return randint(10,30)


    def ulti(self):
        if randint(1,100) % 2 == 0:
            return 40
        else:
            return 0
        



karakter1 = input("1.Oyuncu ismi:")
karakter2 = input("2.Oyuncu ismi:")

oyuncu1 = Karakter(karakter1)

oyuncu2 = Karakter(karakter2)

oyunBitti = 0

print(f"Oyun başlıyor\n############  {oyuncu1.ad} VS {oyuncu2.ad}  ############")

while ( not oyunBitti == 1):

    hamle1 = int(input(f"{oyuncu1.ad} sıra sende \nSaldır = 1\nUlti = 2\nHamle:"))
    print("---------")


    print("""
        {}                    {}
            O                     O
          __|__ ------->         \|/
            |                     |
           / \                   / \\
    
                                                """.format(oyuncu1.ad,oyuncu2.ad))

    

    if(hamle1 == 1):

        oyuncu2.can = oyuncu2.can - oyuncu1.saldır()
        if oyuncu2.can <= 0 :
            oyuncu2.can = 0
        if oyuncu2.can == 0:
            break
    
    else:

        ulti = oyuncu1.ulti()
        if ulti == 0:
            print("BAŞARAMADIK ABİ :( ")
        else:
            oyuncu2.can = oyuncu2.can - ulti

            if oyuncu2.can <= 0 :
                oyuncu2.can = 0
            if oyuncu2.can == 0:
                break
    
    print(f"{oyuncu1.ad} = {oyuncu1.can}  {oyuncu2.ad} = {oyuncu2.can}\n\n\n")



    hamle2 = int(input(f"{oyuncu2.ad} sıra sende \nSaldır = 1\nUlti = 2\nHamle:"))
    print("---------")



    print( """
        {}                     {}
            O                     O
           \|/     <---------   __|__
            |                     |
           / \                   / \\
    
                                                """.format(oyuncu1.ad,oyuncu2.ad))


    if(hamle2 == 1):
    
        oyuncu1.can = oyuncu1.can - oyuncu2.saldır()
        if oyuncu1.can <= 0 :
            oyuncu1.can = 0
            if oyuncu1.can == 0:
                break
    
    else:

        ulti = oyuncu2.ulti()
        if ulti == 0:
            print("BAŞARAMADIK ABİ :( ")
        else:
            oyuncu1.can = oyuncu1.can - ulti
            if oyuncu1.can <= 0 :
                oyuncu1.can = 0
            if oyuncu1.can == 0:
                break


    print(f"{oyuncu1.ad} = {oyuncu1.can}  {oyuncu2.ad} = {oyuncu2.can}\n\n\n")


if(oyuncu1.can == 0 or oyuncu2.can == 0):
    oyunBitti = 1

    if oyuncu1.can == 0:
        print(f"OYUN BİTTİ KAZANAN {oyuncu2.ad.upper()}")
    else:
        print(f"OYUN BİTTİ KAZANAN {oyuncu1.ad.upper()}")
