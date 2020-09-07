dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']
b_text = []
text = input()
a_text = text.split()
for i in range(len(a_text)):
    if a_text[i] in dictionary:
        pass
    else:

        b_text.append(a_text[i])
print('\n'.join(b_text)) if len(b_text) > 0 else print("OK")