def isPrime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

try:
    number = int(input("请输入一个整数："))
    if isPrime(number):
        print(f"{number} 是质数")
    else:
        print(f"{number} 不是质数")
except ValueError:
    print("输入错误，请输入一个有效的整数。")
