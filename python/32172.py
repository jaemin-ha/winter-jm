# 백준 32172 현권이와 신기한 수열
# 그냥 리스트로 푸니 바로 시간 초과 났음 -> set을 이용

N = int(input())

# 확인을 set으로 만들어서 시간 단축
visited = set()
s = 0

# N = 0 이면 안 돌아가므로 s = 0
for i in range(1, N+1):
    visited.add(s)
    nxt = s - i

    # 로직 확인
    if nxt < 0 or nxt in visited:
        nxt = s + i

    s = nxt

print(s)