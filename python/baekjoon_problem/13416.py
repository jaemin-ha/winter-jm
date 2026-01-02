# 백준 13416 주식 투자
T = int(input())

for tc in range(T):
    N = int(input())
    # 출력값
    money = 0

    for _ in range(N):
        A, B, C = map(int, input().split())

        # 양수가 존재하는 경우에만 더함
        if A > 0 or B > 0 or C > 0:
            money += max(A, B, C)

    print(money)