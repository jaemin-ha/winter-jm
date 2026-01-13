# 백준 34921 덕후

A, T = map(int, input().split())

P = 10 + 2 * (25 - A + T)

if P < 0:
    P = 0

print(P)