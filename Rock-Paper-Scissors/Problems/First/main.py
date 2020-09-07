# read test_file.txt
file = open('test_file.txt', 'r', encoding='utf-16')
a = file.readlines()
a = a[0]
a.strip("\n")
print(a)
file.close()