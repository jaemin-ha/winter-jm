### 백준 25756 방어률 무시 계산하기
##  1초 이내

N = int(input())

potions = list(map(int, input().split()))

# 방어률 무시 수치
V = 0

for i in range(N):
    # 계산 과정
    per = (1 - potions[i] / 100)

    V = 1 - (1 - V) * per

    print(V * 100)