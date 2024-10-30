num=int(input("Enter no of integers to be inputed in list"))
List=[]
for i in range(num):
    element=int(input("Enter  integer"))
    List.append(element)
sum1=sum(List)
print(sum1)

