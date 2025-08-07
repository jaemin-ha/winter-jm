### 백준 9663 N-QUEEN
### 10초

import sys
input = sys.stdin.readline

# 이상 없는 지 확인
def check(row):
    for col in range(row):
        if visited[row] == visited[col]:
            return False

        # 대각선 : visited[i] = j -> i번째 행에 j열에 놓음
        # visited 차이는 열 차이, row - col 은 행 차이 둘이 같다는 의미가 대각선에 위치한다는 말
        # abs는 왼쪽이랑 오른쪽비교해야하므로
        if abs(visited[row] - visited[col]) == abs(row - col):
            return False

    return True

def dfs(row):
    global cnt
    # 모두 놓으면 끝
    if row == N:
        cnt += 1
        return

    for col in range(N):
        visited[row] = col
        if not check(row):
            continue

        dfs(row + 1)

N = int(input())
visited = [0] * N
cnt = 0

dfs(0)
print(cnt)