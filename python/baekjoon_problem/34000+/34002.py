### 백준 34002 임스의 잠수맵
##  1초

import sys
from math import ceil

# 분 당 경험치
A, B, C = map(int, sys.stdin.readline().split())

# 입장권 개수
S, V = map(int, sys.stdin.readline().split())

# 현재 레벨
L = int(input())

exp = (250 - L) * 100
time = 0

# VIP 사우나
max_c_exp = C * V * 30

if exp <= max_c_exp:
    # 분 단위 기준이므로 나눠지지 않는다면 올림해야함
    print(ceil(exp / C))
    # 종료 함수
    sys.exit()

exp -= max_c_exp
time += V * 30

# 심신 수련관
max_b_exp = B * S * 30

if exp <= max_b_exp:
    print(time + ceil(exp / B))
    sys.exit()

exp -= max_b_exp
time += S * 30

# 이벤트 맵
time += ceil(exp / A)

print(time)