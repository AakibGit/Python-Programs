class first:
    def __init__(self):
        print("First class")

class second:
    def __init__(self):
        print("second class")

class third(first,second):
    def __init__(self):
        print("third class")
        super().__init__()

    def func(self):
        print("Third class function")

class fourth(third,second):
    def __init__(self):
        print("Fourth class")
        super().func()


obj = fourth()

