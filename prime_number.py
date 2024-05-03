def input_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("正の整数を入力してください。")
            else:
                return value
        except ValueError:
            print("整数を入力してください。")

a = input_int("aの値を入力: ")
b = input_int("bの値を入力: ")

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

if is_prime(a):
    print(f"a = {a} は素数です。")
else:
    print(f"a = {a} は素数ではありません。")

if is_prime(b):
    print(f"b = {b} は素数です。")
else:
    print(f"b = {b} は素数ではありません。")
