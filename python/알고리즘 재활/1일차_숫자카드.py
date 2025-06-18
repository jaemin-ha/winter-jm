T = int(input())

for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input()))
    
    # 빈도 수 기록
    COUNT = [0] * 10

    for i in range(N):
        COUNT[nums[i]] += 1

    # 최대 빈도 카드 찾기
    max_card = 0
    max_v = COUNT[0]

    for i in range(1, 10):
        if COUNT[i] >= max_v:
            max_v = COUNT[i]
            max_card = i

    print(f'#{tc} {max_card} {max_v}')
