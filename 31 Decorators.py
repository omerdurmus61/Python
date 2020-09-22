def func(new_func):
    print("fonksiyon başladı")
    new_func()
    print("fonskiyon bitti")

def hello_func():
    print("merhaba dünya")

func(hello_func)


def new_func():
    def new_func2():
        print("new func 2")
    
    return new_func2()

new_string = new_func()

new_string