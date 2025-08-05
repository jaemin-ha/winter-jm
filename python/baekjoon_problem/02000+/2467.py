### 백준 2467 용액
### 1초

### 투 포인터

import sys
input = sys.stdin.readline

N = int(input())
solutions = list(map(int, input().split()))

min_v = float('inf')

### 범위 설정
s = 0
e = N - 1

while s < e:
    ans = solutions[s] + solutions[e]
    
    if min_v >= abs(ans):
        min_v = abs(ans)
        min_1, min_2 = solutions[s], solutions[e]

    # 결과값에 따른 분리
    if ans == 0:
        break

    elif ans > 0:
        e -= 1
    
    else:
        s += 1

print(min_1, min_2)