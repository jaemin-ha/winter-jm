### 백준 2576 홀수
## 1초 이내

import sys

min_v = float('inf')
result = 0

# 7개만 받음
for i in range(7):
    N = int(sys.stdin.readline())
    if N % 2 == 1:
        result += N
        if min_v > N:
            min_v = N
    else:
        continue

if result == 0:
    print(-1)
else:
    print(result)
    print(min_v)