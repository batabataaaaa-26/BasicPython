import random
import math

a = int(input("a の値を入力: "))
b = int(input("b の値を入力: "))

# Q3
def gcd(a, b):
    while b != 0:
        tmp = b
        b = a % b
        a = tmp
    return a

print("Q3. ({}, {})の最大公約数は{}".format(a, b, gcd(a, b)))

# Q4
def are_coprime(a, b):
    return gcd(a, b) == 1

if are_coprime(a, b):
    print("Q4. {}と{}は互いに素です".format(a, b))
else:
    print("Q4. {}と{}は互いに素ではありません".format(a, b))

# extra
total_combinations = 100000
coprime_count = 0

for _ in range(total_combinations):
    a = random.randint(1, 10000)
    b = random.randint(1, 10000)
    if are_coprime(a, b):
        coprime_count += 1

probability = coprime_count / total_combinations
expected_probability = 6 / (math.pi ** 2)

print("extra. 10万組の自然数の組み合わせにおける互いに素である確率")
print("期待される確率 (6/π^2):", expected_probability)
print("計算された確率:", probability)
