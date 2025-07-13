### 백준 1822 차집합
##  2초 이내

##  시간 복잡도
##  O(N + M + K log K)

import sys

N, M = map(int, sys.stdin.readline().split())
A = set(map(int, sys.stdin.readline().split()))
B = set(map(int, sys.stdin.readline().split()))

# 증가하는 순서
result = sorted(A - B)

# 출력
if not result:
    print(0)
else:
    print(len(result))
    print(*result)