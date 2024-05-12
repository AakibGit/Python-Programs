def hi(name):
    print("how are you "+name)
    

print(__name__)

if __name__ == "__main__":
    name = input("Submit your name: ")
    hi(name)