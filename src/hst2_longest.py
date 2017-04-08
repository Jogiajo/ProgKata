def longest(sentence):
    max1 = 0
    longest_word = max(sentence.split(), key=len)
    print (longest_word)


longest("This is Andela")