from math import sin,pi,sqrt,exp
# --example--
# print(sin(0))
# >>> 0
# -----------



# 台形積分を計算する関数
import math

def trapezoidal_integration(f, a, b, n):
    delta_x = (b - a) / n
    approx_integral = 0
    for i in range(n):
        x1 = a + i * delta_x
        x2 = a + (i + 1) * delta_x
        area = (delta_x / 2) * (f(x1) + f(x2))
        approx_integral += area
    return approx_integral

# 課題1
def task1():
    def sin_function(x):
        return math.sin(x)
    
    a = 0
    b = math.pi / 2
    n = 50
    result = trapezoidal_integration(sin_function, a, b, n)
    return result

# 課題2
def task2():
    def func2(x):
        return 4 / (1 + x**2)
    
    a = 0
    b = 1
    n = 100
    result = trapezoidal_integration(func2, a, b, n)
    return result

# 課題3
def task3():
    def func3(x):
        return math.sqrt(math.pi) * math.exp(-x**2)
    
    a = -100
    b = 100
    n = 1000
    result = trapezoidal_integration(func3, a, b, n)
    return result

# 3つの課題を実行
result1 = task1()
result2 = task2()
result3 = task3()

print("課題1: sin(x)関数の[0, π/2]における積分値の近似:", result1)
print("課題2: 関数 4 / (1 + x^2) の[0, 1]における積分値の近似:", result2)
print("課題3: 関数 √π * exp(-x^2) の[-100, 100]における積分値の近似:", result3)