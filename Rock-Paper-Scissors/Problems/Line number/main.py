# read sample.txt and print the number of lines
line = 0
file = open('sample.txt', 'r')
for _ in file:
    line += 1
print(line)
file.close()
