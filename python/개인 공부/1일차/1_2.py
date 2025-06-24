import sys
import heapq

sys.stdin = open("input.txt", "r")

# 상, 하, 좌, 우
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

N, M = map(int, sys.stdin.readline().split())
dist = [[float('inf')] * M for _ in range(N)]
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 다익스트라 함수 (시작점, 도착점)
def dijkstra(sr, sc, er, ec):
    hq = []
    heapq.heappush(hq, (board[sr][sc], sr, sc))

    # 시작점 비용 초기화
    dist[sr][sc] = board[sr][sc]

    while hq:
        cost, tr, tc = heapq.heappop(hq)

        # 도착점 도달했을 경우
        if tr == er and tc == ec:
            return cost

        # 꺼낸 cost 값이 더 크다면 무시
        if dist[tr][tc] < cost:
            continue

        for d in range(4):
            nr = tr + dr[d]
            nc = tc + dc[d]

            # 범위 고려
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue

            # 누적 비용 계산
            new_cost = cost + board[nr][nc]

            # 더 짧은 경로가 발견된 경우
            if new_cost < dist[nr][nc]:
                dist[nr][nc] = new_cost
                heapq.heappush(hq, (new_cost, nr, nc))

result = dijkstra(0, 0, N - 1, M - 1)

print(result)
