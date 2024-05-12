class a:
    def __init__(self):
        pass

    def func1(self):
        print("class a function")

    def same(self):
        print("Same function in a class")

class b(a):
    def __init__(self):
        print("Constructor of b class")

    def func2(self):
        print("class b function")
    def same(self):
        print("Same function in b class")


obj = b()
obj.same()