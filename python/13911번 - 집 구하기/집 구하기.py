### 그냥 다익스트라는 시간 초과
### 맥도날드 지점에서 최단거리는 시간 너무 오래 걸림
### -> 가상 매장(모든 매장과 연결된 지점)을 추가해서 가상 매장 노드에서 집으로 이동
### -> 이 거리가 최소되는 걸 구함

### 계속 틀리는 이유 : 가상노드와 매장 사이의 도로를 양방향으로 만들었음
### -> 가상노드에서 매장으로 가는 길만 만듬 -> 매장에서 가상노드를 만들면, 가상노드에서 다른 매장으로 이동 가능하게 됨


import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().split())

# 도로 -> 가상 지점 2개 추가 : V+1 -> V+3
adj_lst = [[] for _ in range(V+3)]

# 도로 정보
for _ in range(E):
    u, v, w = map(int, input().split())
    adj_lst[u].append((v, w))
    adj_lst[v].append((u, w))

# 맥도날드
M, m_limit = map(int, input().split())
M_lst = list(map(int, input().split()))

# 가상 지점
mac_node = V+1
# 거리 0으로 도로 만들기
for m in M_lst:
    adj_lst[mac_node].append((m, 0))


# 스타 벅스
S, s_limit = map(int, input().split())
S_lst = list(map(int, input().split()))

# 가상 지점
star_node = V+2
# 거리 0으로 도로 만들기
for s in S_lst:
    adj_lst[star_node].append((s, 0))


# 다익스트라 최단 거리 구하기
def dijkstra(s):
    INF = 10**15
    distance = [INF] * (V+3)
    q = []
    heapq.heappush(q, (0, s))
    distance[s] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for next_node, cost in adj_lst[now]:
            new_dist = dist + cost
            if new_dist < distance[next_node]:
                distance[next_node] = new_dist
                heapq.heappush(q, (new_dist, next_node))
    
    return distance

answer = 10**15

mac_dist = dijkstra(mac_node)
star_dist = dijkstra(star_node)

for i in range(1, V+1):
    # 매장은 넘김
    if i in M_lst or i in S_lst:
        continue

    # 제한 거리 확인
    if mac_dist[i] <= m_limit and star_dist[i] <= s_limit:
        answer = min(answer, mac_dist[i] + star_dist[i])

if answer != 10**15:
    print(answer)
else:
    print(-1)