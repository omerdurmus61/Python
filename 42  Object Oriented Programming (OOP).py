class My_teacher():

    ders = "Teknoloji"

    def __init__(self,name,age,branch):
        self.name = name
        self.age = age
        self.brance = branch


    def word(self):
        print(f"Kendi kanatları ile uçmayanlar Hürkuş olamazlar. {self.name}")

teacher = My_teacher("Vecihi Hürkuş",40,"airplane")

print(teacher.name , teacher.age , teacher.brance)

print(teacher.ders)
teacher.word()