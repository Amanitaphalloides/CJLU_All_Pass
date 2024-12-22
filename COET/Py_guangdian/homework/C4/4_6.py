import random

def simulate_monty_hall(trials):
    switch_wins = 0
    stay_wins = 0

    for _ in range(trials):
        # 随机选择一扇门放汽车，其余放山羊
        doors = [0, 1, 2]
        car_door = random.choice(doors)
        player_choice = random.choice(doors)

        # 主持人打开一扇山羊门
        host_opens = [door for door in doors if door != car_door and door != player_choice][0]

        # 参赛者更换选择
        remaining_doors = [door for door in doors if door != player_choice and door != host_opens]
        player_switches = remaining_doors[0]

        # 判断是否获胜
        if player_switches == car_door:
            switch_wins += 1
        else:
            stay_wins += 1

    return switch_wins / trials, stay_wins / trials

trials = 100000
switch_probability, stay_probability = simulate_monty_hall(trials)
print("更换选择后获胜的概率：", switch_probability)
print("坚持选择后获胜的概率：", stay_probability)
