from math import sin,pi,sqrt,exp
# --example--
# print(sin(0))
# >>> 0
# -----------



# 台形積分を計算する関数
def trapezoidal_integral_sin(a, b, n):
    # 区間の幅
    delta_x = (b - a) / n
    # 積分値の初期化
    integral = 0.0
    # 台形積分を計算
    for i in range(n):
        x0 = a + i * delta_x
        x1 = a + (i + 1) * delta_x
        integral += (sin(x0) + sin(x1)) * delta_x / 2

    return integral
# 区間 [0, π/2] の分割数
n = 50
# 区間 [0, π/2] における台形積分を計算
result = trapezoidal_integral_sin(0, pi/2, n)
# 結果の出力
print("sin(x)の[0, π/2] における積分値（台形積分）:", result)



def trapezoidal_integral(f, a, b, n):
    # 区間の幅
    delta_x = (b - a) / n

    # 積分値の初期化
    integral = 0.0

    # 台形積分を計算
    for i in range(n):
        x0 = a + i * delta_x
        x1 = a + (i + 1) * delta_x
        integral += (f(x0) + f(x1)) * delta_x / 2

    return integral

# 対象の関数
def target_function(x):
    return 4 / (1 + x**2)

# 区間 [0, 1] の分割数
n = 100

# 区間 [0, 1] における台形積分を計算
result = trapezoidal_integral(target_function, 0, 1, n)

# 結果の出力
print("関数 4 / (1 + x^2) の [0, 1] における積分値（台形積分）:", result)


def trapezoidal_integral(f, a, b, n):
    # 区間の幅
    delta_x = (b - a) / n

    # 積分値の初期化
    integral = 0.0

    # 台形積分を計算
    for i in range(n):
        x0 = a + i * delta_x
        x1 = a + (i + 1) * delta_x
        integral += (f(x0) + f(x1)) * delta_x / 2

    return integral

# 対象の関数
def target_function(x):
    return sqrt(pi) * exp(-x**2)

# 区間 [-100, 100] の分割数
n = 1000

# 区間 [-100, 100] における台形積分を計算
result = trapezoidal_integral(target_function, -100, 100, n)

# 結果の出力
print("関数 √π * exp(-x^2) の [-100, 100] における積分値（台形積分）:", result)
