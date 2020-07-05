# Save the input in this variable
ticket = input()
# Add up the digits for each half
first_1 = str(ticket[0])
sec_1 = str(ticket[1])
third_1 = str(ticket[2])
first_2 = str(ticket[-3])
sec_2 = str(ticket[-2])
third_2 = str(ticket[-1])
half1 = int(first_1) + int(sec_1) + int(third_1)
half2 = int(first_2) + int(sec_2) + int(third_2)

# Thanks to you, this code will work
if half1 == half2:
    print("Lucky")
else:
    print("Ordinary")
