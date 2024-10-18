text=input("Enter a text")

def count_words(text):
    
    # Normalize and split the text into words
    words = text.lower().split()
    
    # Count occurrences using a dictionary
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
            
    return word_count


result = count_words(text)
print(result)

