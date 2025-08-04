### 백준 2110 공유기 설치
### 2초

### 완전 탐색으로 풀었지만, 시간초과
### 새로운 방법 검색 -> 이진 탐색

import sys
input = sys.stdin.readline

N, C = map(int, input().split())

houses = []
for _ in range(N):
    house = int(input())
    houses.append(house)

houses.sort()

def can_place(min_dist):
    # 첫번째 집에선 무조건 설치
    cnt = 1

    last_pos = houses[0]

    for i in range(1, N):
        # 거리보다 멀다면 설치하기
        if houses[i] - last_pos >= min_dist:
            cnt += 1
            last_pos = houses[i]

    return cnt >= C

s = 1
e = houses[-1] - houses[0]      # 가장 먼 거리
ans = 0

while s <= e:
    mid = (s + e) // 2
    # 설치 가능하면, 답 후보로 저장
    # 거리 늘리기
    if can_place(mid):
        ans = mid
        s = mid + 1
    # 불가능하다면, 거리 줄이기
    else:
        e = mid - 1

print(ans)