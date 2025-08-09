### 백준 1865 웜홀
### 2초 이내

### 웜홀 가중치를 -로 하는 것은 떠올렸으나, 다음 로직을 몰랐음
### 벨만 포드

import sys
input = sys.stdin.readline

T = int(input())

for tc in range(1, T+1):
    # 지점, 도로, 웜홀
    N, M, W = map(int, input().split())

    road = []

    # 도로
    for _ in range(M):
        s, e, t = map(int, input().split())
        road.append((s, e, t))
        road.append((e, s, t))
    # 웜홀
    for _ in range(W):
        s, e, t = map(int, input().split())
        road.append((s, e, -t))
    
    # 거리 저장
    dist = [0] * (N+1)

    # 답 여부
    cycle = False

    for i in range(1, N+1):
        updated = False
        for s, e, t in road:
            # 거리가 작아진다면, 갱신
            if dist[e] > dist[s] + t:
                dist[e] = dist[s] + t
                updated = True
                # 마지막에서 갱신이 된다면, 음수 사이클이 존재한다는 거
                if i == N:
                    cycle = True
                    break

        # 이번 라운드에 갱신 없다면 결과가 안 바뀜
        if not updated:
            break

    if cycle:
        print('YES')
    else:
        print('NO')