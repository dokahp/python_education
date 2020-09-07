text = input()

text = text.split()
out = []
for i in range(len(text)):
    if 'WWW.' in text[i] or 'www' in text[i] or 'https://' in text[i] or 'http://' in text[i]:
        out.append(text[i])
print("\n".join(out))
