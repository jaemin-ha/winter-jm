T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    # 결과값
    result = 0
    # 시작, 끝
    s = e = N//2

    for r in range(N):
        # 시작부터 끝까지
        for c in range(s, e+1):
            result += arr[r][c]
    
        # 위쪽이라면, 시작 -= 1, 끝 += 1
        if r < N//2:
            s -= 1
            e += 1
        # 중간부터 아래라면, 시작 += 1, 끝 -= 1
        else:
            s += 1
            e -= 1

    print(f'#{tc} {result}')