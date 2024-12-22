import random

def guess_number():
    target = random.randint(0, 9)
    attempts = 0

    while True:
        try:
            guess = int(input("请输入你猜的数字（0-9）："))
            if guess < 0 or guess > 9:
                print("请输入一个0到9之间的整数。")
                continue
            attempts += 1
            if guess == target:
                print(f"预测{attempts}次，你猜中了！")
                break
            elif guess > target:
                print("遗憾，太大了")
            else:
                print("遗憾，太小了")
        except ValueError:
            print("请输入一个有效的整数。")


if __name__ == "__main__":
    guess_number()
