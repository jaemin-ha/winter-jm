T = int(input())

for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    cnt1 = 0
    cnt2 = 0
    cnt3 = 0

    # 가로
    for r in range(9):
        s = 0
        for c in range(9):
            s += arr[r][c]

        if s == 45:
            cnt1 += 1

    # 세로
    for c in range(9):
        s = 0
        for r in range(9):
            s += arr[r][c]

        if s == 45:
            cnt2 += 1

    # 네모
    for r in range(0, 9, 3):
        for c in range(0, 9, 3):
            s = 0
            for i in range(3):
                for j in range(3):
                    s += arr[r+i][c+j]

            if s == 45:
                cnt3 += 1

    result = 0

    if cnt1 == cnt2 == cnt3 == 9:
        result = 1

    print(f'#{tc} {result}')