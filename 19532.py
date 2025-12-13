# 백준 19532 수학은 비대면강의입니다
# 1초
# x, y가 범위가 2000이길래 -> 3000만을 안 넘을 것 같아서 그냥 진행

a, b, c, d, e, f = map(int, input().split())

for x in range(-999, 1000):
    for y in range(-999, 1000):
        if (a*x + b*y == c) and (d*x + e*y == f):
            print(x, y)
            break