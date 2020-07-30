a = int(input())
b = int(input())
i = 0
summa = 0
for x in range(a, b + 1):
    if x % 3 == 0:
        summa += x
        i += 1
print(summa / i)
