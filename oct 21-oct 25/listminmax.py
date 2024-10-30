
num=int(input("Enter no of integers to be inputed"))
integers=[]
for i in range(num):
    integer=int(input("Enter  integer"))
    integers.append(integer)
length=len(integers)
print("length of list is",length)
low=min(integers)
print("lowest of list is",low)
high=max(integers)
print("highest of list is",high)
sort=sorted(integers)
print("sorted list is",sort)
sort.reverse()
print("reversed list is ",sort)
sum1=sum(integers)
print("sum of list is ",sum1)

