### 백준 2206 벽 부수고 이동하기
### 2초 이내

### 첨에 bfs 2개 돌려서 하려고 했는데 -> 시간 초과
### bfs 1개로 할 수 있는 방법 알아내서 고민

import sys
from collections import deque
input = sys.stdin.readline

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

def bfs():
    # visited 구성 -> [[0, 0], [0, 0], [0, 0], [0, 0]] * 6 -> 첫번째는 벽을 안 부술 경우 기록, 두번째는 부서진 거 기록
    # visited[r][c][0] : 벽을 안 부순 상태
    # visited[r][c][1] : 벽을 1번 부순 상태
    visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
    q = deque()
    q.append((0, 0, 0))
    visited[0][0][0] = 1

    while q:
        r, c, broken = q.popleft()
        
        # 종료 조건
        if r == N-1 and c == M-1:
            return visited[r][c][broken]

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
                
            # 범위 없애기
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue
            
            # 1. 벽이 아니고, 방문 X
            if board[nr][nc] == 0 and visited[nr][nc][broken] == 0:
                visited[nr][nc][broken] = visited[r][c][broken] + 1
                q.append((nr, nc, broken))

            # 2. 벽이고, 아직 안 부쉈다면 -> 부수기
            elif board[nr][nc] == 1 and broken == 0 and visited[nr][nc][1] == 0:
                visited[nr][nc][1] = visited[r][c][0] + 1
                q.append((nr, nc, 1))
    
    return -1


N, M = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(N)]

print(bfs())