# 백준 11256 사탕

T = int(input())

for tc in range(T):
    j, N = map(int, input().split())

    box = []
    cnt = 0

    for _ in range(N):
        R, C = map(int, input().split())
        box.append(R*C)

    box.sort(reverse=True)


    for i in range(N):
        j -= box[i]
        cnt += 1

        if j <= 0:
            break

    print(cnt)