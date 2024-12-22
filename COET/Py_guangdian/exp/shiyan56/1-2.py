import math

def fun(x, n):
    result = 0
    for i in range(n + 1):
        result = result + x ** i / math.factorial(i)
    print(result)


fun(2, 4)
