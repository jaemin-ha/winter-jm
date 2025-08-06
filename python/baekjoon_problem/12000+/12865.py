### 백준 12865 평범한 배낭
### 2초

### DP 이용 문제, 무게별로 DP를 짜는 게 기억이 안났음

import sys
input = sys.stdin.readline

N, K = map(int, input().split())

# 인덱스 맞추기위해
bags = [[]]

for _ in range(N):
    W, V = map(int, input().split())
    bags.append((W, V))

# 무게 별로 기록
dp = [[0] * (K+1) for _ in range(N+1)]

for i in range(1, N+1):
    w, v = bags[i]
    for j in range(1, K+1):
        # 현재 물건이 가방 무게 제한을 넘으면, 이전 값 그대로 가져옴
        if w > j:
            dp[i][j] = dp[i-1][j]
        # 현재 물건을 넣는 경우와 안 넣는 경우 중 더 큰 가치 선택
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)

print(dp[N][K])
