import sys
import heapq

sys.stdin = open("input.txt", "r")

N, M, P = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N + 1)]           # 정방향 그래프: P → 각 마을 (돌아오는 길)
reverse_graph = [[] for _ in range(N + 1)]   # 역방향 그래프: 각 마을 → P (가는 길)

# 도로 정보 입력
for _ in range(M):
    from_node, to_node, cost = map(int, sys.stdin.readline().split())
    graph[from_node].append((cost, to_node))           # 정방향
    reverse_graph[to_node].append((cost, from_node))   # 역방향

# 다익스트라 함수 (최단 거리 배열 반환)
def dijkstra(start, g):
    dist = [float('inf')] * (N + 1)
    dist[start] = 0
    hq = []
    heapq.heappush(hq, (0, start))

    while hq:
        cost, current_node = heapq.heappop(hq)

        if dist[current_node] < cost:
            continue

        for next_cost, next_node in g[current_node]:
            new_cost = cost + next_cost
            if new_cost < dist[next_node]:
                dist[next_node] = new_cost
                heapq.heappush(hq, (new_cost, next_node))

    return dist

# 각 마을 → P (가는 길)
go = dijkstra(P, reverse_graph)

# P → 각 마을 (돌아오는 길)
back = dijkstra(P, graph)

costs = []

# 각 학생의 왕복 시간 계산
for start in range(1, N + 1):
    total_time = go[start] + back[start]
    costs.append(total_time)

print(max(costs))
