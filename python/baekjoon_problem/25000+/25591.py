# 백준 25591 푸앙이와 종윤이

A, B = map(int, input().split())

a = 100 - A
b = 100 - B

c = 100 - (a + b)
d = a * b
q = d // 100
r = d % 100
front = c
back = d

if d > 9:
    front = c + q
    back = r

print(a, b, c, d, q, r)
print(front, back)