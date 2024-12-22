f = open('0803.csv', 'r', encoding='utf-8')

user = []

for line in f:
    user.append(line.strip('\n'))

f.close()

for item in user:
    print(item)
