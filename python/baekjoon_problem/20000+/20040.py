### 백준 20040 사이클 게임
### 1초

### 유니온 파인드 기본 문제

import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 초기화
def make_set(n):
    return [x for x in range(n)]

# Find 함수 (경로 압축)
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

# Union 함수
def union(parent, a, b):
    root_a = find(parent, a)
    root_b = find(parent, b)

    # 사이클 생김
    if root_a == root_b:
        return False
    parent[root_b] = root_a
    return True

N, M = map(int, input().split())
parent = make_set(N)

for turn in range(1, M+1):
    s, e = map(int, input().split())

    if not union(parent, s, e):
        print(turn)
        break

else:
    print(0)