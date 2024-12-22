import os

def load_dictionary(file_path):

    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            return {line.split()[0]: line.split()[1] for line in f.readlines()}
    else:
        open(file_path, 'w').close()
        return {}


def save_dictionary(file_path, dictionary):

    with open(file_path, 'w', encoding='utf-8') as f:
        for word, meaning in dictionary.items():
            f.write(f"{word} {meaning}\n")


def add_word(dictionary):

    english_word = input("请输入英文单词: ").strip()
    chinese_word = input("请输入中文翻译: ").strip()

    if english_word in dictionary:
        print("该单词已添加到字典库")
    else:
        dictionary[english_word] = chinese_word
        print("单词添加成功")


def query_word(dictionary):

    english_word = input("请输入要查询的英文单词: ").strip()

    if english_word in dictionary:
        print(f"{english_word} 的中文翻译是: {dictionary[english_word]}")
    else:
        print("字典库中未找到这个单词")


def main():
    file_path = 'dictionary.txt'
    dictionary = load_dictionary(file_path)

    while True:
        print("\n欢迎使用英文学习词典")
        print("1. 添加单词")
        print("2. 查询单词")
        print("3. 退出")

        choice = input("请选择操作: ").strip()

        if choice == '1':
            add_word(dictionary)
            save_dictionary(file_path, dictionary)
        elif choice == '2':
            query_word(dictionary)
        elif choice == '3':
            print("感谢使用，程序退出。")
            break
        else:
            print("输入有误，请重新选择")


if __name__ == "__main__":
    main()