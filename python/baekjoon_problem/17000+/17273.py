# 백준 17273 카드 공장 (small)

N, M = map(int, input().split())

# 카드 정의
cards = []

# 시작
start = []

for _ in range(N):
    front, back = map(int, input().split())
    cards.append([front, back])
    start.append(front)

# 명령
for _ in range(M):
    num = int(input())

    # 숫자가 num 이하인지 확인
    for i in range(N):
        if start[i] < num:

            # 앞면이라면
            if start[i] == cards[i][0]:
                start[i] = cards[i][1]

            # 뒷면이라면
            else:
                start[i] = cards[i][0]


print(sum(start))