words=input("Enter a list of words separated by spaces: ").split()
longest_word=" "
for word in words:
    if len(word)>len(longest_word):
        longest_word=word
print("Length of longest word:",len(longest_word))
