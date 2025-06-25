### 백준 1913 달팽이
## 2초 이내
## 시간 복잡도 : O(N^2) -> 더 이상 불가능 전체를 채워야 하므로
## 채우면서 K값 찾는 경우 -> 시간을 더 줄이기 가능

import sys

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())

board = [[0] * N for _ in range(N)]

# 하, 우, 상, 좌 순
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

# 시작 좌표, 방향
sr, sc, d = 0, 0, 0

# 시작 숫자 (큰 값부터 진행)
cnt = N * N

# 처음 값 저장
board[sr][sc] = cnt

# 처음이 K일 가능성도 존재
if cnt == K:
    ans_r, ans_c = sr + 1, sc + 1

# 1보다 클 경우 반복
while cnt > 1:
    nr, nc = sr + dr[d], sc + dc[d]

    # 범위를 벗어나거나 이미 지나친 곳은 넘기기(0이 아니라면)
    if nr < 0 or nr >= N or nc < 0 or nc >= N or board[nr][nc] != 0:
        d = (d + 1) % 4
        continue

    # 감소 후 값 저장
    cnt -= 1
    board[nr][nc] = cnt

    # K일 경우
    if cnt == K:
        ans_r, ans_c = nr + 1, nc + 1

    # sr, sc을 변경
    sr, sc = nr, nc

# 배열 출력
for i in board:
    print(*i)

# 좌표값 출력
print(ans_r, ans_c)


