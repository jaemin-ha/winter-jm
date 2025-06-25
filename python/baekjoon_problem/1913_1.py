### 백준 1913 달팽이
## 2초 이내
## 처음 생각한 코드
## 바깥부터 채우고, 나중에 다시 돌면서 값 찾은 후 반환

import sys

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())

board = [[0] * N for _ in range(N)]

# 하, 우, 상, 좌 순
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

sr, sc, d = 0, 0, 0
cnt = N * N

board[sr][sc] = cnt

while cnt > 1:
    nr, nc = sr + dr[d], sc + dc[d]

    if nr < 0 or nr >= N or nc < 0 or nc >= N or board[nr][nc] != 0:
        d = (d + 1) % 4
        continue

    cnt -= 1
    board[nr][nc] = cnt
    sr, sc = nr, nc

for i in board:
    print(*i)

for r in range(N):
    for c in range(N):
        if board[r][c] == K:
            print(r+1, c+1)
            break


