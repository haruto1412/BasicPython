from math import sin,pi
# --example--
# print(sin(0))
# >>> 0
# -----------
N=100

a = 0
b = 1 / (2 * pi)
delta_x = (b - a) / N

# 積分値の初期化
integral = 0.0

# 台形積分を計算
for i in range(N):
    x0 = a + i * delta_x
    x1 = a + (i + 1) * delta_x
    integral += (sin(x0) + sin(x1)) * delta_x / 2

# 結果の出力
print("sin(x)の[0, 1/2π]における積分値（台形積分）:", integral)
