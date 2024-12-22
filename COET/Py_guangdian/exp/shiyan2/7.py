import random

x = random.randint(1, 100)
if x % 2 == 1:
    print('{}是奇数'.format(x))
else:
    print('{}是偶数'.format(x))
