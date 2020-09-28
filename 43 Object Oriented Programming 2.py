class Numbers():
    my_number = 61
    def __init__(self,number=2):
        self.number = number
        self.operation = "squera"
    def squera(self):
        return self.number ** 2

my_variable = Numbers()

print (my_variable.squera())