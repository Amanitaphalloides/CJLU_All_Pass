def count_letter(s, letter):
    s = s.lower()
    letter = letter.lower()
    count = s.count(letter)

    return count

input_string = input("请输入一个字符串：")
input_letter = input("请输入一个字符：")
result = count_letter(input_string, input_letter)
print(f"字母 '{input_letter}' 出现了 {result} 次，在 '{input_string}'中")
