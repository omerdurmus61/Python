def asalMi(sayi):
    a=2
    while a < sayi:
        if sayi % a == 0:
            return 0
        
        a+=1
    
    return 1

def func(num1,num2):
    a = num1
    while a <= num2:
        if asalMi(a):
            print(f"{a} sayisi asal.")
        else :
            print(f"{a} sayisi asal değil.")
    
        a += 1


func(7,12)
