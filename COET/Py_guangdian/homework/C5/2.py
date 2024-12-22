def isOdd(num):
    if num % 2 != 0:
        return True
    else:
        return False

number = int(input("请输入一个整数："))
if isOdd(number):
    print(f"{number} 是奇数")
else:
    print(f"{number} 不是奇数")
