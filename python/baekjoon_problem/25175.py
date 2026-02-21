# 백준 25175 두~~부 두부 두부

N, M, K = map(int, input().split())

# 떨어진 정도
a = K - 3

# 원형 구조이므로 N으로 나눈 나머지만큼 이동
b = a % N

# 계산
c = M + b

# N 이상이면 위치 보정
if c >= N:
    c %= N

# 나머지가 0이면 마지막이므로, N 더하기
if c == 0:
    c += N

print(c)