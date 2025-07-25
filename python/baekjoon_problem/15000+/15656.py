### 백준 15656 N과 M (7)

### 중복 허용

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

nums = list(map(int, input().split()))

nums.sort()

arr = [0] * M

def recur(depth):
    if depth == M:
        print(*arr)
        return
    
    for i in range(N):
        arr[depth] = nums[i]
        recur(depth+1)

recur(0)