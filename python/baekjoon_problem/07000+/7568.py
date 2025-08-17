### 백준 7568 덩치
### 1초 이내

import sys
input = sys.stdin.readline

N = int(input())

weight = []
height = []
result = []


for _ in range(N):
    w, h = map(int, input().split())
    weight.append(w)
    height.append(h)


for i in range(N):
    # 기본 순위 1로 설정
    cnt = 1
    for j in range(N):
        # i가 j보다 작다면 순위 1증가
        if weight[i] < weight[j] and height[i] < height[j]:
            cnt += 1
    result.append(cnt)

print(*result)
