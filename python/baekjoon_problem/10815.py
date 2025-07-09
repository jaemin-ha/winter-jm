### 백준 10815 숫자 카드
##  2초

##  시간복잡도
##  입력 받기 및 set 생성: O(N)
##  검색 및 결과 생성: O(M)
##  출력: O(M)
### 따라서 전체 시간복잡도는 O(N + M)

import sys

N = int(input())

card = set(map(int, sys.stdin.readline().split()))

M = int(input())

search = list(map(int, sys.stdin.readline().split()))

# 결과 출력
result = []

for i in search:
    if i in card:
        result.append(1)
    else:
        result.append(0)

print(*result)