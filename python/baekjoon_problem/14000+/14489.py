# 백준 14489 치킨 두 마리

a, b = map(int, input().split())
chicken = int(input())

s = a + b

if s >= 2 * chicken:
    s -= chicken
    s -= chicken

print(s)