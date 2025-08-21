# 맨 밑이 정해지면 다른 곳이 다 정해짐 -> 옆면만 고려하면 됨
# 주사위 순서는 별로 중요하지 않은 것 같음
# 밑에 오는 것이 3쌍 중 1개

import sys
input = sys.stdin.readline

N = int(input())
lst = []

for _ in range(N):
    dice = list(map(int, input().split()))
    lst.append(dice)

print(lst)