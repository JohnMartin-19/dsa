def word_frequency(sentence):
    words = sentence.replace(".", "").split()
    word_frequency = {}
    
    for word in words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1
    
    return word_frequency

word_frequency('I am Mburu. Being a Mburu, we eat mbuzis')