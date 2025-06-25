import sys
import heapq

sys.stdin = open("input.txt", "r")

# 2차원 배열
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

# 배열 기준 좌표가 아니라 수학적 좌표로 주어짐
Y, X = map(int, sys.stdin.readline().split())

N = int(sys.stdin.readline())

dist = [[float('inf')] * N for _ in range(N)]
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 다익스트라 -> 최단 거리 구하기
def dijkstra(sr, sc):
    hq = []
    heapq.heappush(hq, (board[sr][sc], sr, sc))
    dist[sr][sc] = board[sr][sc]

    while hq:
        cost, tr, tc = heapq.heappop(hq)

        if dist[tr][tc] < cost:
            continue

        for d in range(4):
            nr = tr + dr[d]
            nc = tc + dc[d]

            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue
            
            # 벽인 경우 -> 갈 수 없음
            if board[nr][nc] == -1:
                continue

            new_cost = cost + board[nr][nc]

            if new_cost < dist[nr][nc]:
                dist[nr][nc] = new_cost
                heapq.heappush(hq, (new_cost, nr, nc))

# 배열을 map을 이용해서 각 열에서 최대 값 추출하고, 그 안에서 최대값 구하기
home = max(map(max, board))

# 최대값의 좌표 구하기
def homepoint(home):
    for r in range(N):
        for c in range(N):
            if board[r][c] == home:
                return r, c

er, ec = homepoint(home)

# 시작점에서 시작할 경우 걸리는 거리 구하기
dijkstra(Y, X)

# 종료점이 정해져있으므로 출력
print(dist[er][ec])