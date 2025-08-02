### 백준 1937 욕심쟁이 판다
### 2초

### 전에 나온 공 굴리기랑 비슷한 듯?
### 첨에 BFS로 풀려고 했는데 값이 이상하게 나와서, DFS로 전환 그러나 시간초과
### DP를 이용하여 이미 탐색한 곳이라면 넘어가서 시간을 줄임

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 상하좌우
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

def panda(r, c):
    # 이미 탐색한 좌표는 다시 계산하지 않음
    if dp[r][c] != 0:
        return dp[r][c]

    # 최대 길이
    max_length = 1
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]

        if nr < 0 or nr >= n or nc < 0 or nc >= n:
            continue
        # 이전보다 큰 곳으로만 이동
        if forest[r][c] >= forest[nr][nc]:
            continue

        # 이동 가능하면, 다음 위치 + 1
        length = 1 + panda(nr, nc)
        max_length = max(max_length, length)

    # 최장 이동 경로를 기록
    dp[r][c] = max_length

    return max_length

n = int(input())

forest = [list(map(int, input().split())) for _ in range(n)]

# dp
dp = [[0] * n for _ in range(n)]

# 결과값
max_days = 0

# 모든 좌표 비교
for r in range(n):
    for c in range(n):
        result = panda(r, c)
        max_days = max(max_days, result)

print(max_days)