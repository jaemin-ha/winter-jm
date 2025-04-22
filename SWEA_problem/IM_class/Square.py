T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = []

    # 왼쪽 좌표
    for r1 in range(N):
        for c1 in range(N):

            # 아래쪽 좌표
            for r2 in range(r1, N):
                for c2 in range(c1, N):
                    if arr[r1][c1] == arr[r2][c2]:

                        # 넓이
                        area = (r2-r1+1) * (c2-c1+1)
                        result.append(area)

    # 최대값 구하기
    max_v = max(result)

    # 답 구하기
    cnt = result.count(max_v)

    print(f'#{tc} {cnt}')
