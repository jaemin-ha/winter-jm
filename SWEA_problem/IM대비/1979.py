T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    # 가로
    for r in range(N):
        cnt = 0
        for c in range(N):
            if board[r][c] == 1:
                cnt += 1
                if cnt == K:
                    result += 1
                    if c + 1 < N and board[r][c + 1] == 1:
                        result -= 1
            else:
                cnt = 0

    # 세로
    for c in range(N):
        cnt = 0
        for r in range(N):
            if board[r][c] == 1:
                cnt += 1
                if cnt == K:
                    result += 1
                    if r + 1 < N and board[r + 1][c] == 1:
                        result -= 1
            else:
                cnt = 0


    print(f'#{tc} {result}')