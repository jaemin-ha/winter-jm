### 백준 2606 바이러스
### 1초

import sys

input = sys.stdin.readline

def dfs(v, N):
    visited = [0] * (N+1)
    stack = []

    while True:
        if visited[v] == 0:
            visited[v] = 1
            result.append(v)

        for w in adj_lst[v]:
            if visited[w] == 0:
                stack.append(v)
                v = w
                break

        else:
            if stack:
                v = stack.pop()
            else:
                break

N = int(input())
M = int(input())

adj_lst = [[] for _ in range(N+1)]

for _ in range(M):
    v, w = map(int, input().split())
    adj_lst[v].append(w)
    adj_lst[w].append(v)

result = []

dfs(1, N)

print(len(result)-1)