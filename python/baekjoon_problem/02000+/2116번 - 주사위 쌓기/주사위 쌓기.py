# 맨 밑이 정해지면 다른 곳이 다 정해짐 -> 옆면만 고려하면 됨
# 주사위 순서는 별로 중요하지 않은 것 같음
# 밑에 오는 것이 3쌍 중 1개

import sys
from copy import deepcopy

input = sys.stdin.readline

N = int(input())
total = []

# 맨 밑에 오는 주사위
low_dice = []
dice = list(map(int, input().split()))
low_dice.append([dice[0], dice[5]])
low_dice.append([dice[1], dice[3]])
low_dice.append([dice[2], dice[4]])

result = []

# 나머지 주사위
for _ in range(N-1):
    lst = []
    dice = list(map(int, input().split()))
    lst.append([dice[0], dice[5]])
    lst.append([dice[1], dice[3]])
    lst.append([dice[2], dice[4]])
    total.append(lst)

for i in range(1, 7):
    s_i = i
    new_total = deepcopy(total)
    new_low = deepcopy(low_dice)

    value = i

    # 겹치는 면들 제거하기
    for j in range(N-1):
        for k in range(3):
            if value in new_total[j][k]:
                value = [x for x in new_total[j][k] if x != value][0]
                new_total[j].remove(new_total[j][k])
                break
    
    # 맨 밑 주사위말고 옆 주사위들 계산하기
    cnt = 0
    for r in range(N-1):
        max_v_1 = 0
        for c in range(2):
            if max_v_1 < max(new_total[r][c]):
                max_v_1 = max(new_total[r][c])
        cnt += max_v_1
    
    for a in range(3):
        if s_i in new_low[a]:
            new_low.remove(new_low[a])
            break
    
    # 맨 밑 주사위 계산하기
    max_v_2 = 0
    for a in range(2):
        if max_v_2 < max(new_low[a]):
            max_v_2 = max(new_low[a])
    cnt += max_v_2
    
    result.append(cnt)

print(max(result))