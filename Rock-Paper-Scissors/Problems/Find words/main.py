text = input()
text = text.split()
a = []
for i in range(0, len(text)):
    lal = text[i]
    lal = lal[::-1]
    if lal[0] == 's':
        a.append(text[i])

print("_".join(a))