### 백준 1822 차집합
##  2초 이내

##  처음에 푼 풀이
##  시간 복잡도
##  O(N + M + K log K)

import sys

N, M = map(int, sys.stdin.readline().split())

A = set(map(int, sys.stdin.readline().split()))
B = set(map(int, sys.stdin.readline().split()))

result = set()

for i in A:
    if i not in B:
        # set은 추가하려면 add 사용해야함
        result.add(i)

# 증가하는 순으로 출력해야하므로 리스트로 정렬
lst = list(result)
lst.sort()

if len(result) == 0:
    print(0)
else:
    print(len(result))
    print(*lst)