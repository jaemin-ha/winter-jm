T = int(input())

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

# 괴물 찾기
def monster_search(board, N):
    for r in range(N):
        for c in range(N):
            if board[r][c] == 2:
                return r, c


# 괴물에 의한 광선 발사
def lazer(mr, mc, board, N):
    for d in range(4):
        for k in range(1, N):
            nr = mr + dr[d] * k
            nc = mc + dc[d] * k

            # 범위 넘어가면 패스
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue

            # 벽이면 break하고 다음 방향 탐색
            if board[nr][nc] == 1:
                break

            # 다 통과하면 변화 주기
            board[nr][nc] += 3


# 안전한 칸 개수 세는 함수
def safe_room_search(board, N):
    cnt = 0
    for r in range(N):
        for c in range(N):
            if board[r][c] == 0:
                cnt += 1

    return cnt

for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    mr, mc = monster_search(board, N)
    lazer(mr, mc, board, N)
    result = safe_room_search(board, N)

    print(f'#{tc} {result}')