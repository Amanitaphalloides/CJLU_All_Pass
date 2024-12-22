def factorial(n):
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

sum_factorials = 0
for i in range(1, 11):
    sum_factorials += factorial(i)

print("1!+2!+3!+…+10!的结果是：", sum_factorials)