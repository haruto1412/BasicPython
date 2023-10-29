a = input("a の値を入力: ")
b = input("b の値を入力: ")

# TODO

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    else:
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

# a と b の値を入力
a=int(a)
b=int(b)
# a の素数判定
is_prime_a = is_prime(a)

if is_prime_a:
    print(f"{a} は素数です")
else:
    print(f"{a} は素数ではありません")

# b の素数判定
is_prime_b = is_prime(b)       

if is_prime_b:
    print(f"{b} は素数です")
else:
    print(f"{b} は素数ではありません")
    





def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def are_coprime(a, b):
    greatest_common_divisor = gcd(a, b)
    return greatest_common_divisor == 1

def main():
    a = int(input("自然数 a の値を入力してください: "))
    b = int(input("自然数 b の値を入力してください: "))
    
    if are_coprime(a, b):
        print(f"{a} と {b} は互いに素です")
    else:
        print(f"{a} と {b} は互いに素ではありません")

if __name__ == "__main__":
    main()