index = 0

for number in list(range(0,20)):
    print(f"number:{number} index={index}")
    index+=1


print("*"*50)

for indis, number in enumerate(list(range(5,15))):
    print(f"Listemizde {indis}.indexte bulunan eleman {number} elemanıdır.")
    print("*"*55)
