### 백준 24480 알고리즘 수업 - 깊이 우선 탐색 2
### 1초 이내
### 24479의 내림차순 버전

import sys

# 파이썬의 재귀함수 한도를 늘림
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 재귀함수
def dfs(v):
    global cnt
    cnt += 1
    visited[v] = cnt

    for w in adj_lst[v]:
        if visited[w] == 0:
            dfs(w)

N, M, R = map(int, input().split())
adj_lst = [[] for _ in range(N+1)]
visited = [0] * (N+1)
cnt = 0


for _ in range(M):
    v, w = map(int, input().split())
    adj_lst[v].append(w)
    adj_lst[w].append(v)

# 내림차순으로 정렬
for i in range(1, N+1):
    adj_lst[i].sort(reverse=True)

dfs(R)

# 출력
for i in range(1, N+1):
    print(visited[i])