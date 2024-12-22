from datetime import datetime


def format_birthday(birthday_str):

    birthday = datetime.strptime(birthday_str, "%Y-%m-%d")

    date_formats = [
        "%Y-%m-%d",
        "%d/%m/%Y",
        "%m-%d-%Y",
        "%B %d, %Y",
        "%b %d, %Y",
        "%d %B %Y",
        "%d %b %Y",
        "%A, %B %d, %Y",
        "%a, %b %d, %Y",
        "%Y年%m月%d日",
        "%Y.%m.%d",
        "%d.%m.%Y",
        "%d-%m-%Y",
        "%m/%d/%Y",
        "%Y/%m/%d",
        "%d %B, %Y",
        "%d %b, %Y",
        "%B %d, %Y",
        "%b %d, %Y",
        "%A, %d %B %Y",
        "%a, %d %b %Y",
        "%Y-%j",
        "%Y/%j",
    ]

    for fmt in date_formats:
        try:
            print(birthday.strftime(fmt))
        except ValueError as e:
            print(f"Error with format {fmt}: {e}")

birthday_input = input("请输入你的生日（格式为YYYY-MM-DD）：")
format_birthday(birthday_input)
