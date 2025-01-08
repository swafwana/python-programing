vowels=['a','e','i','o','u']
string=input("Enter a string")
count=0
for letter in string:
    if letter in vowels:
        count=count+1
print(count)
modified_string=''
for letter in string:
    if letter in vowels:
        modified_string+='#'
    else:
        modified_string+=letter
print(modified_string)

    

        
