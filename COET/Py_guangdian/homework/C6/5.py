import random

def simulate_birthdays(num_samples, num_people):
    match_count = 0

    for _ in range(num_samples):
        birthdays = [random.randint(1, 365) for _ in range(num_people)]
        if len(set(birthdays)) != len(birthdays):
            match_count += 1

    return match_count / num_samples

def main():
    num_people = 23
    num_samples_list = [1000, 10000, 100000]

    for num_samples in num_samples_list:
        probability = simulate_birthdays(num_samples, num_people)
        print(
            f"样本数量: {num_samples},至少两人同一天生日概率: {probability:.4f}")

if __name__ == "__main__":
    main()
