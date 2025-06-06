T = int(input())

for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))

    max_v = max(nums)

    min_v = min(nums)

    print(f'#{tc} {max_v-min_v}')