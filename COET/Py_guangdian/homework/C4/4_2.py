def count_characters(input_string):
    count_alpha = 0
    count_digit = 0
    count_space = 0
    count_other = 0

    for char in input_string:
        if char.isalpha():
            count_alpha += 1
        elif char.isdigit():
            count_digit += 1
        elif char.isspace():
            count_space += 1
        else:
            count_other += 1

    return count_alpha, count_digit, count_space, count_other

if __name__ == "__main__":
    input_string = input("请输入一行字符：")
    count_alpha, count_digit, count_space, count_other = count_characters(input_string)
    print("英文字符个数：", count_alpha)
    print("数字个数：", count_digit)
    print("空格个数：", count_space)
    print("其他字符个数：", count_other)
