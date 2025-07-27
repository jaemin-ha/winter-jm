### 백준 31575 도시와 비트코인
### 1초

### 오른쪽과 아래쪽만 이동 가능


import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

dr = [0, 1]
dc = [1, 0]

def dfs(r, c):
    visited[r][c] = 1

    if r == M-1 and c == N-1:
        return True

    for d in range(2):
        nr = r + dr[d]
        nc = c + dc[d]

        if nr < 0 or nr >= M or nc < 0 or nc >= N:
            continue

        if board[nr][nc] == 0:
            continue

        if visited[nr][nc] == 1:
            continue

        if dfs(nr, nc):
            return True

    # 갈 곳이 없으면 False 반환
    return False

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(M)]
visited = [[0] * N for _ in range(M)]

if dfs(0, 0):
    print('Yes')
else:
    print('No')

