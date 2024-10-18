names=[]
num=int(input("Enter the no of names to be inputed"))
for i in range(num):
    name=input("Enter name")
    names.append(name)

a_count=0
for name in names:
    a_count=a_count+name.lower().count('a')
print(a_count)
        
