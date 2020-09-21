a=10

def func(number):
    a=5
    return number*a
print(func(3))
print(a)


print("*"*10)

my_string="omer"

def my_func():
    my_string="can"
    print(f"my_func içindeki my_string = {my_string}")

    def my_func2():
        my_string="durmus"
        print(f"my_func2 içindeki my_strin = {my_string}")
    
    my_func2()

my_func()

print(f"fonksiyon sonunda dönen my_string değeri ={my_string}")

