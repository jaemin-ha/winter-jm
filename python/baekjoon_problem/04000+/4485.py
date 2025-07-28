### 백준 4485 녹색 옷 입은 애가 젤다지?
### 1초

### 아이디어 : 다익스트라 문제 -> 코드가 기억이 안 남

import heapq
import sys

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def dijkstra(sr, sc, gr, gc, cave, N):
    hq = []
    heapq.heappush(hq, (cave[sr][sc], sr, sc))

    visited = [[0] * N for _ in range(N)]
    visited[sr][sc] = 1

    while hq:
        weight, tr, tc = heapq.heappop(hq)

        if tr == gr and tc == gc:
            return weight
        
        for d in range(4):
            nr = tr + dr[d]
            nc = tc + dc[d]

            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue

            if visited[nr][nc]:
                continue

            visited[nr][nc] = 1

            heapq.heappush(hq, (weight + cave[nr][nc], nr, nc))

input = sys.stdin.readline

cnt = 1

while True:
    N = int(input())
    if N == 0:
        break

    cave = [list(map(int, input().split())) for _ in range(N)]

    result = dijkstra(0, 0, N-1, N-1, cave, N)
    print(f'Problem {cnt}: {result}')

    cnt += 1