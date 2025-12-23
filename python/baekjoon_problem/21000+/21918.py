# 백준 21918 전구

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

# 전구 배열
lights = [0] + list(map(int, input().split()))

# 명령어
for _ in range(M):
    a, b, c = map(int, input().split())

    # 분기 처리
    if a == 1:
        lights[b] = c

    elif a == 2:
        for i in range(b, c+1):
            lights[i] = 1 - lights[i]

    elif a == 3:
        for i in range(b, c+1):
            lights[i] = 0

    else:
        for i in range(b, c+1):
            lights[i] = 1

print(*lights[1:])