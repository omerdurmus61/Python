
a = int(input("a değerini giriniz:"))
b = int(input("b değerini giriniz:"))
c = int(input("c değerini giriniz:"))

delta = b**2 - 4*a*c

if delta > 0:

    print("iki farklı Reel kök var")
    kok1=b+(delta**(1/2))/2*a
    kok2=b-(delta**(1/2))/2*a
    print(f"kök1= {kok1:1.2} kök2={kok2:1.2}")
elif delta == 0:
    print("iki reel kök var ve bunlar aynı")
    kok1=b+(delta**(1/2))/2*a
    kok2=b-(delta**(1/2))/2*a
    print(f"kök1= {kok1:1.2} kök2={kok2:1.2}")
elif delta<0:
    print("reel kök yok")
    