import math
T = int(input())

# 중계기 위치 찾기
def LTE(arr, N):
    for r in range(N+1):
        for c in range(N+1):
            if arr[r][c] == 2:
                return r, c

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N+1)]
    hr, hc = LTE(arr, N)

    # 거리 담을 배열
    distance = []

    # 거리 넣기
    for r in range(N+1):
        for c in range(N+1):
            if arr[r][c] == 1:
                dist = math.sqrt((hr - r) ** 2 + (hc - c) ** 2)
                distance.append(dist)

    # 최대값
    max_v = max(distance)

    # 소수일 경우 올림함
    result = math.ceil(max_v)

    print(f'#{tc} {result}')
