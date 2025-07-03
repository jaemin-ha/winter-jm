### 백준 2490 윷놀이
##  1초

import sys

# 3개만 주어짐
for _ in range(3):
    ut = list(map(int, sys.stdin.readline().split()))
    
    # 개수 세기
    cnt = ut.count(0)

    # 분류
    if cnt == 4:
        print('D')
    elif cnt == 3:
        print('C')
    elif cnt == 2:
        print('B')
    elif cnt == 1:
        print('A')
    else:
        print('E')