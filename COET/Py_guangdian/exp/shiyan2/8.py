x = float(input("请输入x的值："))

if 0 <= x <= 8:
    y = x * x + 10
else:
    y = x * x * x - 10

print("y的值为：", y)
