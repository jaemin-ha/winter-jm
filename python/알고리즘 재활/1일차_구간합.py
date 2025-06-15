T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    # 최대값 설정
    max_v = - float('inf')

    # 최소값 설정
    min_v = float('inf')

    # 순회하면서 비교
    for i in range(N - M + 1):
        s = 0
        for j in range(M):
            s += nums[i + j]

        if max_v < s:
            max_v = s

        if min_v > s:
            min_v = s

    print(f'#{tc} {max_v-min_v}')