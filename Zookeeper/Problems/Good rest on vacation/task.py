# put your python code here
duration_in_days = abs(int(input()))
food_per_day = abs(int(input()))
one_way_flight = abs(int(input()))
one_night_hotel = abs(int(input()))
total_food = food_per_day * duration_in_days
total_flight = one_way_flight * 2
hotel_cost = one_night_hotel * (duration_in_days - 1)
print(int(total_food + total_flight + hotel_cost))
