### 백준 15654 N과 M (5)
### 수열이 주어지는 문제
### 중복 허용 안함

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

# 증가하는 순서
nums.sort()

arr = [0] * M
visited = [0] * N

def recur(depth):
    if depth == M:
        print(*arr)
        return
    
    for i in range(len(nums)):
        if visited[i]:
            continue
        
        arr[depth] = nums[i]
        visited[i] = True
        recur(depth+1)
        visited[i] = False

recur(0)