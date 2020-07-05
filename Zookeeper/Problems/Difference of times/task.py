# put your python code here
hours_first_time = abs(int(input()))
minutes_first_time = abs(int(input()))
seconds_first_time = abs(int(input()))
hours_second_time = abs(int(input()))
minutes_second_time = abs(int(input()))
seconds_second_time = abs(int(input()))
print(int((((hours_second_time - hours_first_time) * 3600) + ((minutes_second_time - minutes_first_time) * 60) + (seconds_second_time - seconds_first_time))))
