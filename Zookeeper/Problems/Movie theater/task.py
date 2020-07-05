number_of_halls = abs(int(input()))
capacity = abs(int(input()))
number_of_viewers = abs(int(input()))
capacity_full = number_of_halls * capacity
print(capacity_full >= number_of_viewers)
