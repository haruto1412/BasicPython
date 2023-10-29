#a = input("aの値を入力: ")
#b = input("bの値を入力: ")
#n=int(input("nの値を入力:"))
# TODO
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

# ユーザーから整数を入力して素数判定を行う
try:
    num = int(input("整数を入力してください: "))
    is_prime_result = is_prime(num)
    print(f"{num} は素数です: {is_prime_result}")
except ValueError:
    print("Errar:整数を入力してください")
