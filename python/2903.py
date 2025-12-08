# 백준 2903 중앙 이동 알고리즘

# 횟수
N = int(input())

# 리스트에 담기
lst = [0] * (N+1)

# 초기 값
lst[0] = 2

for i in range(1, N+1):
    lst[i] = lst[i-1] -1 + lst[i-1]

print(lst[N]**2)