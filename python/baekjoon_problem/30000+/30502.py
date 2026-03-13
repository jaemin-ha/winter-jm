# 백준 30502 미역은 식물 아닌데요

N, M = map(int, input().split())

# 광합성 o, x
light_1 = set()

light_2 = set()

# 운동성 o, x
exercise_1 = set()

exercise_2 = set()


for _ in range(M):
    a, b, c = input().split()

    if b == "P":
        if c == "1":
            light_1.add(a)
        else:
            light_2.add(a)
    else:
        if c == "1":
            exercise_1.add(a)
        else:
            exercise_2.add(a)

# 식물
o = light_1 & exercise_2

# 광합성 못하거나 운동성 있으면 식물 아님
x = light_2 | exercise_1

# 최소 : 식물인 것만
min_v = len(o)

# 최대 : 전체에서 x 개수 빼기
max_v = N - len(x)

print(min_v, max_v)