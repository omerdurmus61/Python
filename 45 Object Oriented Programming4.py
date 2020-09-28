class Apple():
    def __init__(self,name):
        self.name = name
    def information(self):
        return self.name +" 100 calories"
    

class Banana():
    def __init__(self,name):
        self.name = name
    def information(self):
        return self.name + " 200 calories"

banana = Banana("banana")
apple = Apple("apple")

fruit_list =[banana,apple]

for fruit in fruit_list:
    print(fruit.information())