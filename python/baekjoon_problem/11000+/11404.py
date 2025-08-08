### 백준 11404 플로이드
### 1초

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

INF = float('inf')
graph = [[INF] * (n+1) for _ in range(n+1)]

for _ in range(m):
    s, e, c = map(int, input().split())
    graph[s][e] = min(graph[s][e], c)


for i in range(1, n+1):
    graph[i][i] = 0

for k in range(1, n+1):
    for r in range(1, n+1):
        for c in range(1, n+1):
            graph[r][c] = min(graph[r][c], graph[r][k] + graph[k][c])

for i in range(1, n+1):
    row = []
    for j in range(1, n+1):
        if graph[i][j] == INF:
            row.append(0)
        else:
            row.append(graph[i][j])
    print(*row)