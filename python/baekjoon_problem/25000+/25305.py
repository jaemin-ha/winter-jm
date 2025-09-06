### 백준 25305 커트라인
### 1초


import sys
input = sys.stdin.readline

N, k = map(int, input().split())
scores = list(map(int, input().split()))

scores.sort(reverse=True)

print(scores[k-1])