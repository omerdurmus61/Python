ogrenciNo=[]
ad=[]
soyad=[]
tel=[]

x=0
while x<3:
    ogrenciNo.append(int(input("No:")))
    ad.append(input("ad:"))
    soyad.append(input("soyad:"))
    tel.append(input("tel:"))
    x+=1

a=0

ogrenciler={ogrenciNo[a]:{"ad":ad[a],"soyad":soyad[a],"tel":tel[a]},
            ogrenciNo[a+1]:{"ad":ad[a+1],"soyad":soyad[a+1],"tel":tel[a+1]},
            ogrenciNo[a+2]:{"ad":ad[a+2],"soyad":soyad[a+2],"tel":tel[a+2]}
    }

print(ogrenciler)