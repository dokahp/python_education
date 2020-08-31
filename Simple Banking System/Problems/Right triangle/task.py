import math


class RightTriangle:
    def __init__(self, hyp, leg_1, leg_2):
        self.c = hyp
        self.a = leg_1
        self.b = leg_2
        # calculate the area here

    def square(self):
        if math.pow(self.c, 2) == math.pow(self.a, 2) + math.pow(self.b, 2):
            print(self.a * self.b / 2)
        else:
            print("Not right")


# triangle from the input
input_c, input_a, input_b = [int(x) for x in input().split()]

# write your code here
triangle = RightTriangle(input_c, input_a, input_b)
triangle.square()
