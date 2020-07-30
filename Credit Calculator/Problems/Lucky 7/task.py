import math
n = int(input())
i = 0
list_of_numbers = list()
for _ in range(n):
    number_input = int(input())
    list_of_numbers.append(number_input)
for i in range(n):
    if list_of_numbers[i] % 7 == 0:
        m = int(math.pow(int(list_of_numbers[i]), 2))
        print(m)