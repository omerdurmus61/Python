def cal(x,y,ops):
    if ops not in ["+","-","*","/"]:
        print("Lütfen operatör seçiniz.")

    elif ops == "+":
        print(f"{x:} + {y} = {x+y:1.2}")
    
    elif ops == "-":
        print(f"{x} - {y} = {x-y:1.2}")

    elif ops == "*":
        print(f"{x} * {y} = {x*y:1.2}")

    elif ops == "/":
        print(f"{x} / {y} = {x/y:1.2}")

x = float(input("x değerini giriniz:"))
y = float(input("y değerini giriniz:"))
opr = input("operatörü giriniz:")

cal(x,y,opr)