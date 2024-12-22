def generate_fibonacci(n):
    # 初始化前两项
    fib_sequence = [1, 1]

    # 生成后续的Fibonacci数列
    for i in range(2, n):
        next_value = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_value)

    return fib_sequence


def main():
    fib_sequence = generate_fibonacci(40)

    # 从第三项开始打印输出并写入文件
    with open("0604.txt", "w") as file:
        for index in range(2, len(fib_sequence)):
            print(fib_sequence[index])
            file.write(f"{fib_sequence[index]}")

if __name__ == "__main__":
    main()
