word = input()
word = word.split()
word = (word[0] + ' ' + ' '.join(word[1:]).title()).replace(' ','')
print(word)