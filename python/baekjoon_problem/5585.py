### 백준 5585 거스름돈
##  1초

# 물건 금액
N = int(input())

# 잔돈 리스트
money = [500, 100, 50, 10, 5, 1]

# 잔돈 금액
remain = 1000 - N

# 잔돈 개수
cnt = 0

# 계산
while remain > 0:
    for i in range(6):
        a = remain // money[i]
        remain -= money[i] * a
        cnt += a

print(cnt)