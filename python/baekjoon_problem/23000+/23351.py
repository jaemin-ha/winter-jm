### 백준 23351 물 주기
### 1초

### 시간 복잡도 : O(K * N^2) 
### => 하루에 드는 연산 : O(N), 최악의 반복일 : O(K * N)

import sys

input = sys.stdin.readline()

N, K, A, B = map(int, input.split())

catnip = [K] * N

day = 0

while True:
    # 물 주는 로직
    min_idx = catnip.index(min(catnip))

    for i in range(min_idx, min_idx+A):
        catnip[i] += B

    # 날짜 증가 시키고, leaf 감소
    day += 1
    catnip = [x-1 for x in catnip]

    # 종료 로직
    if 0 in catnip:
        break
    
print(day)

