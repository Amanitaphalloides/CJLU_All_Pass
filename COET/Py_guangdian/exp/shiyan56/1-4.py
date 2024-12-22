def fun(n):
    s = 0
    for i in range(n):
        if i % 3 == 0 and i % 7 == 0:
            s += i
    return s

result = fun(56)
print(result)
