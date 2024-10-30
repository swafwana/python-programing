import math
start=int(input("Enter the starting range"))
end=int(input("Enter the ending range"))
result=[]
for i in range(int(math.sqrt(start)),int(math.sqrt(end))+1):
    square=i*i
    if 1000<=square<=9999:
        if all(int(digit)%2==0 for digit in str(square)):
            result.append(square)
if result:
        print("four digits perfect squares with all digits even are",result)
else:
        print("no four digits perfect square with all even digits found")

          
