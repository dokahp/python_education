# put your python code here
all_grade = input()
all_grade = all_grade.split()
count = all_grade.count('A')
count = count / len(all_grade)
print(round(count, 2))