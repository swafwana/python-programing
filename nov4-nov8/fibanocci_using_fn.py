def fibanocci(num):
    a=0
    b=1
    print("fibanocci series: ")
    for i in range (num):
        print(a,end=" ")
        a,b=b,a+b
num1=int(input("Enter a number"))
fibanocci(num1)
    



    
