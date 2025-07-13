### 백준 25496 장신구 명장 임스
##  1초


P, N = map(int, input().split())

jangsingu = list(map(int, input().split()))

# 정렬 과정이 필요
jangsingu.sort()

cnt = 0

for i in range(N):

    # 200넘으면 중단

    if P >= 200:
        break

    P += jangsingu[i]
    cnt += 1



print(cnt)