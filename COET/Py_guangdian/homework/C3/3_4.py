def is_palindrome(n):
    str_n = str(n)
    return str_n == str_n[::-1]

num = int(input("请输入一个5位数字： "))

if is_palindrome(num):
    print(f"{num} 是一个回文数")
else:
    print(f"{num} 不是一个回文数")