my_list=[10,20,30,40,50]

for number in my_list:
    print(number)

print("------------")

for number in my_list:
    if number==40:
        break

    print(number)

print("------------")

for number in my_list:
    if number==40:
        continue

    print(number)

print("-----------")

for number in my_list:
    pass
