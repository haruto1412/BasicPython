a = input("aの値を入力: ")
b = input("bの値を入力: ")


a=int(a)
b=int(b)
# TODO
# aの素数判定
is_prime_a = True
if a <= 1:
    is_prime_a = False
elif a <= 3:
    is_prime_a = True
elif a % 2 == 0 or a % 3 == 0:
    is_prime_a = False
else:
    i = 5
    while i * i <= a:
        if a % i == 0 or a % (i + 2) == 0:
            is_prime_a = False
            break
        i += 6

if is_prime_a:
    print(f"{a} は素数です")
else:
    print(f"{a} は素数ではありません")

is_prime_b = True
if b <= 1:
    is_prime_b = False
elif b <= 3:
    is_prime_b = True
elif b % 2 == 0 or b % 3 == 0:
    is_prime_b = False
else:
    i = 5
    while i * i <= b:
        if b % i == 0 or b % (i + 2) == 0:
            is_prime_b = False
            break
        i += 6

if is_prime_b:
    print(f"{b} は素数です")
else:
    print(f"{b} は素数ではありません")
