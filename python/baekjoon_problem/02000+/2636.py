### 백준 2636 치즈
### 1초


from collections import deque
import sys
input = sys.stdin.readline

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]


## 공기들을 표시 -> 처음에는 0, 0으로 시작해서 표시함
def check(pan):
    visited = [[0] * M for _ in range(N)]
    q = deque()
    q.append((0, 0))
    visited[0][0] = 1

    while q:
        r, c = q.popleft()

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue

            if visited[nr][nc]:
                continue

            if pan[nr][nc] == 0:
                visited[nr][nc] = 1
                q.append((nr, nc))

    return visited



## 제거될 치즈 개수 구하기
def cheese_delete(pan):
    air = check(pan)
    melt = []

    for r in range(N):
        for c in range(M):
            # 치즈 중에서 보기
            if pan[r][c] == 1:
                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]

                    if nr < 0 or nr >= N or nc < 0 or nc >= M:
                        continue
                    
                    # 공기가 있으면 녹는 치즈
                    if air[nr][nc] == 1:
                        melt.append((r, c))
                        break

    # melt에 있는 거 다음 시간을 위해 0으로 변경
    for r, c in melt:
        pan[r][c] = 0


    return len(melt)


N, M = map(int, input().split())
pan = [list(map(int, input().split())) for _ in range(N)]

time = 0
last_cheese = 0

while True:
    melt_cheese = cheese_delete(pan)
    if melt_cheese == 0:
        break
    time += 1
    last_cheese = melt_cheese

print(time)
print(last_cheese)