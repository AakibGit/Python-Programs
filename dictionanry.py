
obj = {
    1:"one",
    2:"two",
    3:"three"
}
obj[4]="four"

for k,v in obj.items():
    print(k,v)

print(obj.items())

list = (1,2,4,5,6,"string")

for i in list:
    print(i)


set = {"java","c++","python"}

set.add("c")
set.pop()

for i in set:
    print(i)

l = [1,2,"one","two"]

l.append(3)
l.append("three")
l.pop()
for i in l:
    print(i)