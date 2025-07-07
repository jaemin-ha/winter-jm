### 백준 2953 나는 요리사다
##  1초

import sys

cnt = - float('inf')
max_i = -1

for i in range(1, 5+1):
    scores = list(map(int, sys.stdin.readline().split()))
    if cnt < sum(scores):
        cnt = sum(scores)
        max_i = i

print(max_i, cnt)