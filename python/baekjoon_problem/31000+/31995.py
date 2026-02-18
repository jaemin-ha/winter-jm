# 백준 31995 게임말 올려놓기

N = int(input())
M = int(input())

if N == 1 or M == 1:
    print(0)

else:
    print((N-1) * (M-1) * 2)