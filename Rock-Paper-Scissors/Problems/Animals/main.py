file = open("animals.txt")
another_file = open('animals_new.txt', 'w')
a = file.read()
a = a.split("\n")
for i in range(0, len(a)):
    another_file.write(str(a[i]) + " ")

file.close()
another_file.close()
