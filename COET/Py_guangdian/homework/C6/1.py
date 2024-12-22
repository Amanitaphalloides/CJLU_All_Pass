import random
import string

def generate_password(length=8):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_multiple_passwords(count, length=8):
    return [generate_password(length) for _ in range(count)]

passwords = generate_multiple_passwords(10)
for i, pwd in enumerate(passwords, start=1):
    print(f"密码 {i}: {pwd}")
