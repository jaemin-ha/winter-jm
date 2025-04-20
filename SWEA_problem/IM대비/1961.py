T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]
    # 결과 배열, (1번째, 2번째, 3번째)
    result = [''] * N

    # 1번째
    for c in range(N):
        for r in range(N-1, -1, -1):
            result[c] += arr[r][c]
        # 띄어쓰기 구분
        result[c] += ' '

    for r in range(N-1, -1, -1):
        for c in range(N-1, -1, -1):
            # 0, 1, 2 로 넣기 위해 N-1-r
            result[N-1-r] += arr[r][c]
        # 띄어쓰기 구분
        result[N-1-r] += ' '

    for c in range(N-1, -1, -1):
        for r in range(N):
            # 0, 1, 2 로 넣기 위해 N-1-c
            result[N-1-c] += arr[r][c]

    print(f'#{tc}')
    for line in result:
        print(line)