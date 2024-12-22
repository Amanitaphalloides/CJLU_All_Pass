volume = lambda length, width, height: length * width * height

length = float(input("请输入长方体的长: "))
width = float(input("请输入长方体的宽: "))
height = float(input("请输入长方体的高: "))


print("长方体的体积是:", volume(length, width, height))
