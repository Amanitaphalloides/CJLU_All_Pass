def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    a, b = 1, 1
    for i in range(3, n + 1):
        a, b = b, a + b
    return b

print("Fibonacci数列的第40项是：", fibonacci(40))
