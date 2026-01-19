# 백준 28088 응애(EASY)

# 0, 1 바꾸는 문제로 생각해서 풀었는데 잘 안됐음
# 인사 받는 것으로 바꿔서 코드 간소화
# 파이썬은 시간 초과 -> 파이파이로 제출 -> 원래 목적은 사이클을 찾는?

N, M, K = map(int, input().split())

people = [0] * N

# 처음
state = []

for _ in range(M):
    num = int(input())
    state.append(num)


# 인사 횟수
for _ in range(K):
    # 인사 받은 횟수
    cnt = [0] * N

    # 인사 로직
    for j in state:
        cnt[(j-1) % N] += 1
        cnt[(j+1) % N] += 1

    # 다음에 인사할 사람들
    state = []

    # 1이면 상태 추가
    for i in range(N):
        if cnt[i] == 1:
            state.append(i)

print(len(state))