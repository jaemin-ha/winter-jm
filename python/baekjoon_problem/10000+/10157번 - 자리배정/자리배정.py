### 달팽이 숫자랑 비슷한 문제라고 생각함
### 1부터 채우고, 방향 조절

import sys
input = sys.stdin.readline

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

R, C = map(int, input().split())
N = int(input())

seat = [[0] * R for _ in range(C)]

# 시작 좌표와 방향
sr, sc, d = C-1, 0, 0

# 1부터 시작
cnt = 1

seat[sr][sc] = cnt

# 배열 채우기
while cnt < R * C:
    nr, nc = sr + dr[d], sc + dc[d]

    if nr < 0 or nr >= C or nc < 0 or nc >= R or seat[nr][nc] != 0:
        d = (d + 1) % 4
        continue

    cnt += 1
    seat[nr][nc] = cnt
    sr, sc = nr, nc

er, ec = -1, -1
for r in range(C):
    for c in range(R):
        if seat[r][c] == N:
            er, ec = r, c
            break
    if er != -1:
        break

# 없는 대기번호 물어보는 경우
if N > R * C:
    print(0)
else:
    print(ec + 1, C - er)