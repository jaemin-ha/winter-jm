### 백준 4435 중간계 전쟁
##  1초

import sys

# 입력
score1 = [1, 2, 3, 3, 4, 10]
score2 = [1, 2, 2, 2, 3, 5, 10]

T = int(input())

for tc in range(1, T+1):
    gandalf = list(map(int, sys.stdin.readline().split()))
    sauron = list(map(int, sys.stdin.readline().split()))
    
    # 계산
    cnt1 = 0
    cnt2 = 0

    for i in range(6):
        cnt1 += score1[i] * gandalf[i]

    for i in range(7):
        cnt2 += score2[i] * sauron[i]
    
    # 출력
    if cnt1 > cnt2:
        print(f'Battle {tc}: Good triumphs over Evil')
    elif cnt2 > cnt1:
        print(f'Battle {tc}: Evil eradicates all trace of Good')
    else:
        print(f'Battle {tc}: No victor on this battle field')
