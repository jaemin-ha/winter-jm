import sys
import heapq
input = sys.stdin.readline

# 거리 구하는 함수
def dijkstra(s, e):
    INF = float('inf')
    dist = [INF] * (N+1)
    
    # 처음 값 0 으로 초기화
    dist[s] = 0

    # q에 넣기
    pq = [(0, s)]

    # pq에 존재한다면
    while pq:
        current_dist, now = heapq.heappop(pq)

        # 지금 거리가 더 크다면 넘김
        if current_dist > dist[now]:
            continue
        
        # 다음 갈 곳 고르기
        for nxt, cost in adj_lst[now]:
            new_dist = current_dist + cost

            # 거리 더한 값이 저장된 값보다 작다면 갱신
            if new_dist < dist[nxt]:
                dist[nxt] = new_dist
                heapq.heappush(pq, (new_dist, nxt))
    
    # 목적지의 값 반환
    return dist[e]

N = int(input())
M = int(input())

# 노선 저장 -> 인접 리스트
adj_lst = [[] for _ in range(N+1)]

for _ in range(M):
    s, e, cost = map(int, input().split())
    adj_lst[s].append((e, cost))

qs, qe = map(int, input().split())


print(dijkstra(qs, qe))