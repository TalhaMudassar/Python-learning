def find_word(n, stringar):
    word_len = []
    txt = stringar.split(" ")
    
    for word in txt:
        if len(word) > n:
            word_len.append(word)
            
    return word_len


print(f"Words with length greater than 3 are {find_word(3, 'The quick brown fox jumps over the lazy dog')}")
