money = abs(int(input()))
government_return = 700000
i = 0
while money < government_return:
    money = (money * 0.071) + money
    i += 1

print(i)
