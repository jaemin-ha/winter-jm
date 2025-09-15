### 백준 1712 손익분기점

import sys, math
input = sys.stdin.readline

A, B, C = map(int, input().split())

if C - B == 0:
    print(-1)
else:
    result = (A / (C - B))

    if result <= 0:
        print(-1)
    else:
        print(math.floor(result + 1))

