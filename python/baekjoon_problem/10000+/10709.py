# 백준 10709 기상캐스터
# N, M이 100이라서 크게 신경안씀

# 입력
N, M = map(int, input().split())
weather = [input() for _ in range(N)]

# 출력
result = [[-1] * M for _ in range(N)]

for i in range(N):
    # 구름을 가지고 있는 경우에만 확인
    if "c" in weather[i]:
        # 구름의 위치 값
        k = 100

        for j in range(M):
            # 구름 이라면 0, 시간 0으로 초기화한 후 +1
            if weather[i][j] == "c":
                result[i][j] = 0
                k = j
                cnt = 0
                cnt += 1

            # 구름이 없다면
            else:
                # 위치 값보다 작다면 넘김 -> 동쪽에 구름이 있음
                if j < k:
                    continue

                # 아니라면 -> 구름이 왼쪽에 있었음
                else:
                    result[i][j] = cnt
                    cnt += 1

for i in range(N):
    print(*result[i])