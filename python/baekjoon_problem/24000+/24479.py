### 백준 24479 알고리즘 수업 - 깊이 우선 탐색 1
### 1초
### 파이썬의 재귀한도 1000 -> 재귀한도를 늘려야함 M이 10만이므로
### O(MlogM+N)
### 처음에 스택을 이용해서 풀려고 했는데 시간초과

import sys
# 재귀한도를 늘려야 통과하는 듯
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# DFS
def dfs(v):
    global cnt
    cnt += 1
    # 방문 순서 기록
    visited[v] = cnt

    # 인접한 곳 중 방문안했으면, 재귀
    for w in adj_lst[v]:
        if visited[w] == 0:
            dfs(w)

N, M, R = map(int, input().split())
adj_lst = [[] for _ in range(N+1)]
visited = [0] * (N + 1)
cnt = 0

# 인접 리스트 추가
for i in range(M):
    v, w = map(int, input().split())
    # 양방향
    adj_lst[v].append(w)
    adj_lst[w].append(v)

# 오름차순이므로 정렬
for i in range(1, N+1):
    adj_lst[i].sort()

dfs(R)

for i in range(1, N+1):
    print(visited[i])