list1=[4,2,3]
list2=[1,5,3]
if len(list1)==len(list2):
    print("Lists are of same length")
else:
    print("lists are not of same length")
if sum(list1)==sum(list2):
    print("Sum of lists are same")
else:
    print("Sum of lists doesn't sum up to same sum")
#flag=0
x=len(list1)
y=len(list2)
for i in range (x):
    for j in range (y):
        if list1[i]==list2[j]:
                   #flag=flag+1
                   print(list1[i],"occur in both")
                   
                   
