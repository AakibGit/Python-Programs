print("python working successfully ")

age = int(input("Enter age\n"))

if age>=18:
    print("vote")
else:
    print("can't vote")
    
    
def fact(n):
    
    i=1;
    f=1;
    
    while i<=n:
        f = f *i
        i = i+1
        
    # for i in range(1,n+1):
    #     f=f*i
        
    return f 

print(fact(5))   