A = abs(int(input()))
B = abs(int(input()))
H = abs(int(input()))

if A <= H <= B:
    print("Normal")
if H > B:
    print("Excess")
if H < A:
    print("Deficiency")
