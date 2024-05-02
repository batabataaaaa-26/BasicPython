a = int(input("a の値を入力: "))
b = int(input("b の値を入力: "))

# TODO
def gcd(a, b):
    while b != 0:
        tmp = b
        b = a % b
        a = tmp
    return a

print("({}, {})の最大公約数は{}".format(a, b, gcd(a, b)))
