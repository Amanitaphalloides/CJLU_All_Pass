import math

def calculate_hypotenuse(a, b):
    return math.sqrt(a ** 2 + b ** 2)

a = 3
b = 4

c = calculate_hypotenuse(a, b)

print("斜边长为:", c)
