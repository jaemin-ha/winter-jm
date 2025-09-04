### 백준 11723 집합
### 1.5초

### 그냥 풀었는데 해결
### 집합 사용법을 정확히 숙지하기
### remove는 값이 없을 경우 에러가 날 수 있지만, discard는 에러를 넘김

import sys
input = sys.stdin.readline

M = int(input())

S = set()

for _ in range(M):
    order = input().split()
    
    if order[0] == 'add':
        S.add(int(order[1]))

    elif order[0] == 'check':
        if int(order[1]) in S:
            print(1)
        else:
            print(0)
    
    elif order[0] == 'remove':
        S.discard(int(order[1]))

    elif order[0] == 'toggle':
        if int(order[1]) in S:
            S.remove(int(order[1]))
        else:
            S.add(int(order[1]))
    
    elif order[0] == 'all':
        S = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
             11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
    
    elif order[0] == 'empty':
        S = set()