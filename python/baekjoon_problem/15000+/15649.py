### 백준 15649 N과 M (1)
### 순열


import sys

input = sys.stdin.readline()

N, M = map(int, input.split())

arr = [0] * M

# 중복 X -> 방문 처리
visited = [0] * (N+1)

def recur(depth):
    if depth == M:
        print(*arr)
        return
    
    for i in range(1, N+1):
        if visited[i]:
            continue

        arr[depth] = i
        visited[i] = True
        recur(depth+1)
        visited[i] = False

recur(0)