fp = open('0801.txt', 'r')

s = fp.read()

fp.close()

ls = s.splitlines()

for item in ls:
    print(item, end=' ')
