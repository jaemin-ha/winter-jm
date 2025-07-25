### 백준 15655 N과 M (6)

### 중복 제외, 순열 (1 7, 1 8, 1 9, 7 8, 7 9)

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

nums = list(map(int, input().split()))

nums.sort()

arr = [0] * M

def recur(depth, prv):
    if depth == M:
        print(*arr)
        return
    
    for i in range(prv, N):
        arr[depth] = nums[i]
        recur(depth+1, i+1)

recur(0, 0)