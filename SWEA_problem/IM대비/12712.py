T = int(input())

# 가로, 세로
dr1 = [1, -1, 0, 0]
dc1 = [0, 0, 1, -1]

# 대각선
dr2 = [1, 1, -1, -1]
dc2 = [1, -1, -1, 1]

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_v = - float('inf')

    # 가로, 세로
    for r in range(N):
        for c in range(N):
            s = arr[r][c]

            for d in range(4):
                for k in range(1, M):
                    nr = r + dr1[d] * k
                    nc = c + dc1[d] * k
                    if nr < 0 or nr >= N or nc < 0 or nc >= N:
                        continue

                    s += arr[nr][nc]

            if max_v < s:
                max_v = s
    
    # 대각선
    for r in range(N):
        for c in range(N):
            s = arr[r][c]

            for d in range(4):
                for k in range(1, M):
                    nr = r + dr2[d] * k
                    nc = c + dc2[d] * k
                    if nr < 0 or nr >= N or nc < 0 or nc >= N:
                        continue

                    s += arr[nr][nc]

            if max_v < s:
                max_v = s

    print(f'#{tc} {max_v}')