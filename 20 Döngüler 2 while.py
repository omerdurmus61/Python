p=0
while p<20:
    if (p<10) and (p%2==0):
        print("p={} sayisi 10'dan küçük bir çift sayıdır.".format(p))
    elif (p<10) and (p%2!=0):
        print("p=",p,"sayisi 10'dan küçük bit tek sayıdır.")
    elif (p==10) or (p==11):
        pass 
    elif (p>11) and (p<15):
        print(f"p:{p}. Continue çalıştı")
        p+=1
        continue
        print("Merhaba continue")
    else:
        print(f"p:{p}.Break çalıştı")
        break
        print("merhaba break")

    p+=1
