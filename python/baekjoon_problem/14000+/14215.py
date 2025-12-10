# 백준 14215 세 막대

a, b, c = map(int, input().split())

max_v = max(a, b, c)
remain = a + b + c - max_v

# 두 변의 합이 큰 변보다 커야함
while max_v >= remain:
    max_v -= 1

print(remain + max_v)