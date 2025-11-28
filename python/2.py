### 백준 10775 공항
### 시간 초과 -> 유니온 파인드

import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    
    return parent[x]

# 게이트 수
G = int(input())

# 비행기 수
P = int(input())

parent = [i for i in range(G+1)]
planes = []
result = 0

# 비행기 추가
for _ in range(P):
    airplane = int(input())
    planes.append(airplane)

for plane in planes:
    # 비행기 번호가 게이트보다 큰 경우를 고려해야함
    if plane > G:
        plane = G

    root = find(plane)

    # root가 0이면 도킹 불가능
    if root == 0:
        break

    # 도킹 성공 경우 : root -= 1
    parent[root] = root - 1

    result += 1

print(result)