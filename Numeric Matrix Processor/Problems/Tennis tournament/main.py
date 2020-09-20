number = int(input())
a = [input().split() for x in range(number)]
a = [x[0] for x in a if x[1] == 'win']
print(a)
print(len(a))