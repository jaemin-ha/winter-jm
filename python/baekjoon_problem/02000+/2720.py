# 백준 2720 세탁소 사장 동혁
# 문제에 달러가 아니라 센트이길래 달러로 구하려고 했으나
# 소수점으로 인해 값이 달라짐
# -> 그냥 센트로 나누는 것이 정수로 쉽게 구하는 방법

T = int(input())

for _ in range(T):
    lst = [0] * 4
    n = int(input())

    if n >= 25:
        a = n // 25
        lst[0] += int(a)
        n -= a * 25

    if n >= 10:
        b = n // 10
        lst[1] += int(b)
        n -= b * 10

    if n >= 5:
        c = n // 5
        lst[2] += int(c)
        n -= c * 5

    if n >= 1:
        d = n // 1
        lst[3] += int(d)
        n -= d * 1

    print(*lst)