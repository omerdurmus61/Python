class Class1():
    def __init__(self):
        print("Class1 crated")
    def method1(self):
        print("method1")
    def method2(self):
        print("method2")



class Class2():
    def __init__(self):
        Class1.__init__(self)
        print("Class2 crated")
    def method3(self):
        print("method3")
    def method1(self):
        print("Class2 method1")
my_instance2 = Class2()

my_instance2.method1()


