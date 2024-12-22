from random import randint

ls = [randint(10, 99) for i in range(20)]

fp = open('0801.txt', 'w')

for i in range(20):
    fp.write(str(ls[i]) + '\n')

fp.close()
