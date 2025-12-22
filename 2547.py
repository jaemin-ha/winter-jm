# 백준 2547 사탕 선생 고창영

T = int(input())

for tc in range(T):
    # 공백
    gap = input()

    # 학생 수
    N = int(input())
    # 사탕 개수
    cnt = 0

    for _ in range(N):
        candy = int(input())
        cnt += candy

    if cnt % N == 0:
        print("YES")
    else:
        print("NO")