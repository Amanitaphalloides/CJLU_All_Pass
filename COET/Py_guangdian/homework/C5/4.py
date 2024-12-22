def multi(*args):
    product = 1
    for num in args:
        product *= num
    return product

input_numbers = input("请输入多个数字，用空格分隔：")
numbers = map(int, input_numbers.split())
result = multi(*numbers)
print("乘积是：", result)
