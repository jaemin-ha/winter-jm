### 백준 11053 가장 긴 증가하는 부분 수열
### 1초

### 처음은 그냥 무지성 비교로 해봤는데
### 이거 반례 걸려서 고민 중 도움 받아서 dp를 이용하였습니다. 
'''
5
10 16 11 12 30
'''

import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

# 최소값이 1이므로 1개일 때
dp = [1] * N

for i in range(N):
    for j in range(i):
        # 지금 nums[i]의 값이 더 크다면, 비교해서 갱신
        if nums[j] < nums[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))