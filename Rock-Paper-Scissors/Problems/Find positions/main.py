# put your python code here
sequence = input()
sequence = sequence.split()
x = input()
out = []
if sequence.count(x) == 0:
    print('not found')
else:
    for i in range(0, len(sequence)):
        if sequence[i] == x:
            out.append(str(i))
    print(' '.join(out))
