### 인접까지는 생각
### 부모 노드를 찾는 과정을 고민

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
adj_lst = [[] for _ in range(N+1)]

for _ in range(N-1):
    n1, n2 = map(int, input().split())
    adj_lst[n1].append(n2)
    adj_lst[n2].append(n1)

# 방문 처리
visited = [0] * (N+1)

def bfs(start):
    # 덱에 처음 시작을 추가
    deq = deque([start])

    while deq:
        node = deq.popleft()

        # 1부터 시작하므로 먼저 만나는 쪽이 부모라고 알 수 있음
        for next in adj_lst[node]:
            if visited[next] == 0:
                visited[next] = node
                deq.append(next)

# 루트가 1이라고 말해줌
bfs(1)

# 2번부터 출력
result = visited[2:]
for x in result:
    print(x)