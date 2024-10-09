word=input("Enter a word")
vowels='aeiou'
found_vowel=[]
for char in word:
    if char in vowels:
          found_vowel.append(char)
if found_vowel:
        print("vowels found are",found_vowel)
else:
        print("No vowels are found")

