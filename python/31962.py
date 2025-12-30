# 백준 31962 등교

# 버스 대수, 제한시간
N, M = map(int, input().split())
lst = []

for _ in range(N):
    S, T = map(int, input().split())

    # 제한 시간보다 작은 것만 추가
    if S + T <= M:
        lst.append(S)


# 출력
if len(lst) > 0:
    print(max(lst))

else:
    print(-1)