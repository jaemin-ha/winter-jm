### 백준 15650 N과 M (2)
### 조합

import sys

input = sys.stdin.readline()

N, M = map(int, input.split())

arr = [0] * M

def recur(depth, prv):

    if depth == M:
        print(*arr)
        return
    
    for i in range(prv, N+1):
        arr[depth] = i
        recur(depth+1, i+1)

recur(0, 1)