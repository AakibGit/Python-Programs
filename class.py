class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print(f"The name of student is {self.name}")
        print(f"the age of student is {self.age}")
    def func(self):
        print("Function inside class")

class classromm:
    def __init__(self):
        super().__init__()


s = student("python",19)

s.func()

c = classromm()
