# 백준 30889 좌석 배치도

screen = [["."] * 21 for _ in range(10)]

N = int(input())

for _ in range(N):
    seat = input()

    screen[ord(seat[0]) - 65][int(seat[1:])] = "o"


for i in range(10):
    print("".join(screen[i][1:]))