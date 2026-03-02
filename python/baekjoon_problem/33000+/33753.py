# 백준 33753 주차 요금 정산하기

from math import ceil

A, B, C = map(int, input().split())
T = int(input())

# 30분 미만일 경우
if T <= 30:
    print(A)

else:
    T -= 30
    a = ceil(T / B) * C
    print(A + int(a))