# 백준 20494 스시

N = int(input())
lst = [0] * 26

for _ in range(N):
    sonim = input()

    for sushi in sonim:
        lst[ord(sushi) - 65] += 1

print(sum(lst))