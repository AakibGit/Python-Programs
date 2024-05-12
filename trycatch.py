num1 = int(input("Enter First number\n"))
num2 = int(input("Enter Second number\n"))

try:
    num3 = num1 / num2
    print(num3)
    
# except Exception as e:
except Exception as e:
    print(e)

except:
    print("Exception occurs")
        
finally:
    print("This will work always ")
    
    
        