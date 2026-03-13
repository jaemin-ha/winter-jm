# 백준 1652 누울 자리를 찾아라

N = int(input())

board = [list(input()) for _ in range(N)]

garo = 0
sero = 0

# 가로
for r in range(N):
    cnt = 0
    for c in range(N):

        # 빈 공간인지
        if board[r][c] == ".":
            cnt += 1

        # 아니라면 cnt 확인해서 추가
        # cnt 초기화
        else:
            if cnt >= 2:
                garo += 1
            cnt = 0

    # 그냥 비거나, 끝나면 확인
    if cnt >= 2:
        garo += 1

# 세로
for c in range(N):
    cnt = 0
    for r in range(N):
        if board[r][c] == ".":
            cnt += 1

        else:
            if cnt >= 2:
                sero += 1
            cnt = 0

    if cnt >= 2:
        sero += 1

print(garo, sero)