### 백준 16236 아기 상어
### 2초

# 아이디어 과정
# 1. 상어 위치
# 2. 먹을 물고기가 없으면 return
# 3. 먹이 찾는 로직
# - 거리를 기록하여 가장 가까운 곳으로 가는 방법 -> 이걸 몰라서, 고민함
# 좀 더 정리를 한 후, 풀어야 할 것 같음 -> 바로 코드로 가니, 코드가 안 적혀서 오래 걸림

import sys
from collections import deque
input = sys.stdin.readline

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def shark(sr, sc):
    global shark_cm
    time = 0
    eat = 0
    space[sr][sc] = 0

    while True:
        visited = [[-1] * N for _ in range(N)]
        q = deque()
        q.append((sr, sc))
        visited[sr][sc] = 0

        # 먹이
        eats = []
        min_dist = None

        while q:
            tr, tc = q.popleft()

            for d in range(4):
                nr, nc = tr + dr[d], tc + dc[d]

                # 범위
                if nr < 0 or nr >= N or nc < 0 or nc >= N:
                    continue

                # 방문한 곳
                if visited[nr][nc] != -1:
                    continue

                # 큰 물고기는 못 지나감
                if space[nr][nc] > shark_cm:
                    continue

                visited[nr][nc] = visited[tr][tc] + 1
                dist = visited[nr][nc]

                if min_dist is not None and dist > min_dist:
                    continue

                # 먹이 후보
                if 0 < space[nr][nc] < shark_cm:
                    eats.append((dist, nr, nc))
                    min_dist = dist
                    
                # 먹이가 아니라면 이동만
                else:
                    q.append((nr, nc))

        # 먹을 게 없다면 return
        if not eats:
            return time

        # 거리, 행, 열 순으로 우선순위해서 제일 작은 것으로 이동
        dist, nr, nc = min(eats)
        # 거리 증가
        time += dist
        sr, sc = nr, nc
        space[sr][sc] = 0

        # 상어 크기 증가
        eat += 1
        if eat == shark_cm:
            shark_cm += 1
            eat = 0

N = int(input())
space = [list(map(int, input().split())) for _ in range(N)]

# 아기 상어 위치 찾기
for r in range(N):
    for c in range(N):
        if space[r][c] == 9:
            sr, sc = r, c
            break

# 상어 크기
shark_cm = 2

result = shark(sr, sc)

print(result)