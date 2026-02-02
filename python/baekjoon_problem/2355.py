# 백준 2355 시그마

A, B = map(int, input().split())

# B가 A보다 크다는 조건 X -> 고려해줘야함
if A > B:
    A, B = B, A

l = B - A + 1
s = A + B

if l % 2 == 0:
    result = (l // 2) * s

else:
    result = (l // 2) * s + (s // 2)

print(result)