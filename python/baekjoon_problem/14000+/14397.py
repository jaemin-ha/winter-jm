# 백준 14397 해변
# 처음에 방향을 일일이 적으려고 했으나 잘 안됐음 -> 1. 홀수, 짝수 구분, 2. 범위 벗어나는 것 지우기
# 방향을 미리 리스트에 적음

N, M = map(int, input().split())
beach = [input() for _ in range(N)]

# 방향 적기
# 홀수 위,아래
odd = [(-1, 0), (-1, 1), (1, 0), (1, 1)]
# 짝수 위, 아래
even = [(-1, -1),(-1, 0), (1, -1), (1, 0)]
# 양 옆
side = [(0, -1), (0, 1)]

length = 0

for i in range(N):
    for j in range(M):
        # 가지치기
        if beach[i][j] != "#":
            continue

        # 대각
        if i % 2 == 1:
            d = odd
        else:
            d = even

        for di, dj in d:
            ni, nj = i + di, j + dj

            if ni < 0 or ni >= N or nj < 0 or nj >= M:
                continue

            if beach[ni][nj] == ".":
                length += 1


        # 양 옆
        for di, dj in side:
            ni, nj = i + di, j + dj

            if ni < 0 or ni >= N or nj < 0 or nj >= M:
                continue

            if beach[ni][nj] == ".":
                length += 1

print(length)