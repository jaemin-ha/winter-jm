### 배낭 문제

## 예시 입력
'''
4
3
1 1 1 1
10 20 30 40
'''

import sys

sys.stdin = open('input.txt', 'r')

# 물건 개수
n = int(sys.stdin.readline())
# 최대 무게
W = int(sys.stdin.readline())

weight = list(map(int, sys.stdin.readline().split()))
value = list(map(int, sys.stdin.readline().split()))

# 무게 w에서 최대 가치
dp = [[0] * (W + 1) for _ in range(n + 1)]

# DP 테이블 채우기 (Bottom-Up 방식)
# 1번부터 n번까지
for i in range(1, n+1):
    # 배낭 무게 모두 고려
    for w in range(W+1):
        # 현재 물건을 넣을 수 없는 경우(초과)
        if w < weight[i-1]:
            # 이전 상태를 가져옴
            dp[i][w] = dp[i-1][w]
        # 가능한 경우
        else:
            # 안 넣었을 때 최대 가치와 넣었을 때 가치 중 더 큰 것을 선택
            dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight[i-1]] + value[i-1])

# 최대 무게 w일 때 최대 가치
print(dp[n][w])

# print(dp)