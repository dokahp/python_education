# put your python code here
class_a = abs(int(input()))
class_b = abs(int(input()))
class_c = abs(int(input()))
new_desk_a = class_a % 2
if new_desk_a > 0:
    new_desk_a = (class_a // 2) + 1
else:
    new_desk_a = class_a // 2
new_desk_b = class_b % 2
if new_desk_b > 0:
    new_desk_b = (class_b // 2) + 1
else:
    new_desk_b = class_b // 2
new_desk_c = class_c % 2
if new_desk_c > 0:
    new_desk_c = (class_c // 2) + 1
else:
    new_desk_c = class_c // 2
print(int(new_desk_a + new_desk_b + new_desk_c))
