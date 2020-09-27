#Bankamatik

hesapOmer = {
    'ad':'Ömer Can Durmuş',
    'hesapNo':'12345678961',
    'bakiye':3000,
    'ekHesap':2000
}

hesapTaha = {
    'ad':'Taha Ertuğrul Polat',
    'hesapNo':'12345678906',
    'bakiye':4000,
    'ekHesap':3000
}

def paraCek(hesap,miktar):
    print(f"Merhaba {hesap['ad']} işleminiz gerçekleştirilecek.")

    if hesap['bakiye'] >= miktar:
        print(f"Hesabınızdan çekmek istediğiniz miktar {miktar}TL hesabınızda bulunuyor.Dilerseinz çekebilirsiniz.(e/h)  ")

        cevap = input ("Cevabınız:")

        if cevap == "e" or cevap == "E":
        
            hesap['bakiye'] = hesap['bakiye'] - miktar

            print(f"Çekilen miktar {miktar} TLYeni bakiyeniz {hesap['bakiye']}TL")
        else:
            print("İşlem kapatıldı.")


    elif   hesap['bakiye']+hesap['ekHesap'] >= miktar:

        print(f"Hesabınızdan çekmek istediğiniz miktar {miktar}TL hesabınızda bulunmuyor. Dilerseniz ek hesaptan çekebilirsiniz.(e/h)   ")

        cevap = input ("Cevabınız:")

        if cevap == "e" or cevap == "E" :

            fark = miktar - hesap['bakiye']
            hesap['bakiye'] = 0
            hesap['ekHesap'] = hesap['ekHesap']-fark
            print(f"Çekilen miktar {miktar} .Bakiyeniz 0TL ek hesap bakiyeniz {hesap['ekHesap']}TL")
        else :
            print("İşlem kapatıldı.")
    
    else :
        print("Bu miktarda para çekemzsiniz.")



hesapNo = int ( input("Lütfen hesap numaranızı giriniz:") )

if hesapNo == 12345678961:
    
    print(f"Merhaba {hesapOmer['ad']}\nİşleminizi seçiniz:\nPara çekme:1\nPara yatırma:2")

    islem = int (input("islem numarası:"))

    if islem == 1:
        
        miktar = int (input("Çekilecek miktar:"))

        paraCek(hesapOmer,miktar)
    
    elif islem == 2:
        pass



elif hesapNo == 12345678906:

    print("İşleminizi seçiniz:\nPara çekme:1\nPara yatırma:2")

    islem = int (input("islem numarası:"))

    if islem == 1:
        
        miktar = int (input("Çekilecek miktar:"))

        paraCek(hesapTah,miktar)

