T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    customers = list(map(int, input().split()))
    cnt = [0] * 11112

    for customer in customers:
        cnt[customer] += 1

    ans = 'Possible'
    bread = 0

    for t in range(11112):
        # 빵 생산
        if t != 0 and t % M == 0:
            bread += K
        
        # 사람 수가 빵보다 많으면
        if cnt[t] > bread:
            ans = 'Impossible'
            break
        
        # 빵 감소
        bread -= cnt[t]

    print(f'#{tc} {ans}')
