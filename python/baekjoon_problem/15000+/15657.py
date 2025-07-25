### 백준 15657 N과 M (8)

### 중복 허용, 앞에 나온 것보다 뒤에 것이 작으면 안됨

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

nums = list(map(int, input().split()))
nums.sort()

arr = [0] * M

# 조건 확인
def check(depth):
    if depth == 0:
        return True
    
    if arr[depth-1] <= arr[depth]:
        return True
    else:
        return False


def recur(depth):
    if depth == M:
        print(*arr)
        return
    
    for i in range(N):
        arr[depth] = nums[i]
        if check(depth):
            recur(depth+1)

recur(0)