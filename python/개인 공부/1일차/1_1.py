import sys
import heapq

sys.stdin = open("input.txt", "r")

N, T = map(int, sys.stdin.readline().split())
dist = [float('inf')] * N
v = [[] for _ in range(N)]

for _ in range(T):
    from_node, to_node, cost = map(int, sys.stdin.readline().split())
    v[from_node].append((cost, to_node))

## 다익스트라 함수 (시작점, 종료점)
def dijstra(start, end):
    hq = []
    dist[start] = 0
    heapq.heappush(hq, (0, start))
    while hq:
        cost, num = heapq.heappop(hq)
        # 정상적으로 종료될 시 비용 반환
        if num == end:
            return cost

        if dist[num] < cost:
            continue

        for next_cost, next_num in v[num]:
            total_cost = cost + next_cost
            if total_cost < dist[next_num]:
                dist[next_num] = total_cost
                heapq.heappush(hq, (total_cost, next_num))

    # 도착점에 도달 못하는 상황이면 impossible 반환
    return "impossible"

result = dijstra(0, N-1)

print(result)
