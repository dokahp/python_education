N = abs(int(input()))
R = abs(int(input()))
i = 0
T = 12
while N > R:
    N = N / 2
    i += 1
T *= i
print(T)
