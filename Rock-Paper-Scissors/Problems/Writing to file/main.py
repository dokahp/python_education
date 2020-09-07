f_name = 'test.txt'
my_string = "A string to be written to a file!"
file = open('test.txt', 'w')
# what to do with the file and the string
print(my_string, file=file)
file.close()
