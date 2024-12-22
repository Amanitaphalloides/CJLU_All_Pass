def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

if __name__ == "__main__":
    num1 = int(input("请输入第一个整数："))
    num2 = int(input("请输入第二个整数："))
    print("最大公约数是：", gcd(num1, num2))
    print("最小公倍数是：", lcm(num1, num2))
