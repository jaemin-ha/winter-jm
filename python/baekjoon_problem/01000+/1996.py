# 백준 1996 지뢰 찾기
# N이 1000이어서 그냥 풀어도 될 것이라고 생각

# 크기
N = int(input())

# 입력
board = [list(input()) for _ in range(N)]
# 결과
result = [[0] * N for _ in range(N)]

# 8방향
dr = [1, 1, 1, 0, 0, -1, -1, -1]
dc = [1, 0, -1, 1, -1, 1, 0, -1]

for r in range(N):
    for c in range(N):

        if board[r][c] == ".":
            cnt = 0
            for d in range(8):
                nr = r + dr[d]
                nc = c + dc[d]

                # 범위 벗어나면 넘김
                if nr < 0 or nr >= N or nc < 0 or nc >= N:
                    continue

                # .이면 넘김
                if board[nr][nc] == ".":
                    continue

                cnt += int(board[nr][nc])

            # 10이상이면 M
            if cnt >= 10:
                result[r][c] = "M"
            else:
                result[r][c] = str(cnt)

        # 지뢰면 *
        else:
            result[r][c] = "*"

for i in range(N):
    print("".join(result[i]))