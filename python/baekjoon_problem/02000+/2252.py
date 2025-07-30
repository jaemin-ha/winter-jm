### 백준 2252 줄 세우기
### 2초

### 위상 정렬

import sys
from collections import deque

input = sys.stdin.readline

def sort(N, graph, lst):
    result = []
    q = deque()
    
    # 0부터 deque에 넣음
    for i in range(1, N+1):
        if lst[i] == 0:
            q.append(i)
    
    # q가 있다면
    while q:
        current = q.popleft()
        # 먼저 결과에 넣음
        result.append(current)
        
        # 결과에 있는 것들 중 -1 하고, 0이면 넣음
        for next_node in graph[current]:
            lst[next_node] -= 1
            if lst[next_node] == 0:
                q.append(next_node)

    return result


N, M = map(int, input().split())
# 진입 차수 계산
lst = [0] * (N+1)
# 인접 리스트로 만듬
graph = [[] for _ in range(N+1)]

# 초기값 준비
for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    lst[e] += 1

result = sort(N, graph, lst)

print(*result)