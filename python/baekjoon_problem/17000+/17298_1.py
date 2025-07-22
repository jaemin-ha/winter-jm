### 백준 17298 완전 탐색 풀이

import sys

N = int(sys.stdin.readline())

nums = list(map(int, sys.stdin.readline().split()))
    
result = []

for i in range(N-1):
    ans = -float('inf')
    for j in range(i, N):
        if nums[i] < nums[j]:
            ans = nums[j]
            result.append(ans)
            break

    if ans == -float('inf'):
        result.append(-1)

result.append(-1)

print(*result)

