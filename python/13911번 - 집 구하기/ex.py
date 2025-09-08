### 가상 노드 없는 다중 다익스트라

import sys, heapq
input = sys.stdin.readline

V, E = map(int, input().split())
adj = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))
    adj[v].append((u, w))

# 맥도날드
M, m_limit = map(int, input().split())
M_lst = list(map(int, input().split()))
M_set = set(M_lst)

# 스타벅스
S, s_limit = map(int, input().split())
S_lst = list(map(int, input().split()))
S_set = set(S_lst)

INF = 10**15

def dijkstra_multi(starts):
    dist = [INF] * (V + 1)
    hq = []
    heappush = heapq.heappush
    heappop = heapq.heappop

    # 이거만 다름
    for s in starts:
        dist[s] = 0
        heappush(hq, (0, s))

    graph = adj
    while hq:
        d, u = heappop(hq)
        if d != dist[u]:
            continue
        for v, w in graph[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heappush(hq, (nd, v))
    return dist

mac_dist  = dijkstra_multi(M_lst)
star_dist = dijkstra_multi(S_lst)

ans = INF
for i in range(1, V + 1):
    # 집 후보는 매장 제외
    if i in M_set or i in S_set:
        continue
    if mac_dist[i] <= m_limit and star_dist[i] <= s_limit:
        s = mac_dist[i] + star_dist[i]
        if s < ans:
            ans = s

print(ans if ans < INF else -1)
