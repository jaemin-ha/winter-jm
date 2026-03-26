# 백준 16428 A/B - 3

A, B = map(int, input().split())

q = A // B
r = A % B

# B가 음수일 경우
# r == 0 이면 += 1 작업 X
if A > 0 and B < 0:
    if r == 0:
        q = q
        r = r
    else:
        r += abs(B)
        q += 1

elif A < 0 and B < 0:
    if r == 0:
        q = q
        r = r
    else:
        r += abs(B)
        q += 1

print(q)
print(r)