# 백준 2581 소수

M = int(input())
N = int(input())

# 소수담을 리스트
lst = []

# 소수 판정 로직
for num in range(M, N+1):
    cnt = 0
    for i in range(1, num+1):
        if num % i == 0:
            cnt += 1

    if cnt == 2:
        lst.append(num)


if len(lst) == 0:
    print(-1)
else:
    print(sum(lst))
    print(lst[0])