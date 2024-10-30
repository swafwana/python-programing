num=int(input("Enter no of integers to be inputed"))
integers=[]
for i in range(num):
    integer=int(input("Enter  integer"))
    integers.append(integer)
    if (integer>100):
        integers[i]="over"
print(integers)
    
                   
