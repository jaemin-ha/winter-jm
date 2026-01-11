# 백준 32866 코인의 신 건모

N = int(input())
X = int(input())

# 현재 금액
current = N * ((100 - X) / 100)

# 구하는 식
# current * (1 + result/100) = N
# result = (N/current - 1) * 100

print((N/current - 1) * 100)