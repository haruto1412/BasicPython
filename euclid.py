a = input("a の値を入力: ")
b = input("b の値を入力: ")

# TODO

a = int(input("a の値を入力: "))

b = int(input("b の値を入力: "))

while b:
    a, b = b, a % b

gcd1 = a

print(f"(1) 最大公約数は {gcd1} です。")