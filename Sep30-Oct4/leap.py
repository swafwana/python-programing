year=int(input("Enter a year"))
for i in range(2024,year+1):
    if(i%4==0 and i%100!=0):
        print(i)
