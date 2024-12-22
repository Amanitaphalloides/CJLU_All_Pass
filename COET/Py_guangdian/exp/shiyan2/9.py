char = input("请输入一个字符：")

if char.isdigit():
    print("这是一个数字字符")
elif 'A' <= char <= 'Z':
    print("这是一个大写英文字符")
elif 'a' <= char <= 'z':
    print("这是一个小写英文字符")
else:
    print("这是其他字符")
