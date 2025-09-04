### 그냥 더하는 방식은 시간 초과
### 누적 합을 이용하여 계산

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

prefix_sum = [0] * (N+1)

for i in range(1, N+1):
    prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]

for _ in range(M):
    s, e = map(int, input().split())
    print(prefix_sum[e] - prefix_sum[s - 1])