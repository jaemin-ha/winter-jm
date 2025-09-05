import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = []
cnt = 0

for _ in range(N):
    coin = int(input())
    coins.append(coin)

# 최소니까 내림차순으로 변경
coins.sort(reverse=True)

for coin in coins:
    # K가 동전보다 크다면
    # 나누고 K를 나머지로 갱신
    if K >= coin:
        cnt += K // coin
        K %= coin

print(cnt)
