T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    # 돌 현재 상태
    rock_list = [0] + list(map(int, input().split()))

    # 뒤집기 진행 M
    for _ in range(M):
        # 시작 돌 i, 범위 j
        i, j = map(int, input().split())
        for k in range(1, j+1):
            # 범위 확인, 같은지 확인
            if i - k >= 1 and i + k < N + 1 and rock_list[i - k] == rock_list[i + k]:
                rock_list[i - k] = 1 - rock_list[i - k]
                rock_list[i + k] = 1 - rock_list[i + k]

    result = rock_list[1:]

    print(f'#{tc}', *result)