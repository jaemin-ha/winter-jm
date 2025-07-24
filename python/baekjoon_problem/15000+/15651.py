### 백준 15651 N과 M (3)
### 중복 순열

import sys

input = sys.stdin.readline()

N, M = map(int, input.split())

arr = [0] * M

def recur(depth):
    if depth == M:
        print(*arr)
        return
    
    for i in range(1, N+1):
        arr[depth] = i
        recur(depth + 1)


recur(0)