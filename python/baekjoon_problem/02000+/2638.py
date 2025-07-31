### 백준 치즈 2638
### 1초

import sys
from collections import deque
input = sys.stdin.readline

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

def check(pan):
    visited = [[0] * M for _ in range(N)]
    q = deque()
    q.append((0,0))
    visited[0][0] = 2

    while q:
        r, c = q.popleft()

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue

            if visited[nr][nc] == 1:
                continue

            if pan[nr][nc] == 0:
                visited[nr][nc] = 1
                q.append((nr, nc))

    return visited



def cheese_delete(pan):
    air = check(pan)
    melt = []

    for r in range(N):
        for c in range(M):
            if pan[r][c] == 1:
                cnt = 0
                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]

                    if nr < 0 or nr >= N or nc < 0 or nc >= M:
                        continue
                    
                    if air[nr][nc] == 1:
                        cnt += 1

                if cnt >= 2:
                    melt.append((r, c))
    
    for r, c in melt:
        pan[r][c] = 0
    
    return len(melt)



N, M = map(int, input().split())
pan = [list(map(int, input().split())) for _ in range(N)]

time = 0

while True:
    last_cheese = cheese_delete(pan)
    if last_cheese == 0:
        break
    time += 1

print(time)