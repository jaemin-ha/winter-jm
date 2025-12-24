# 백준 14235 크리스마스 선물
# 조건 보고 시간 초과 안 날 것 같아서 품
# 정석은 우선순위 큐로 푸는 거인것 같음

import sys
input = sys.stdin.readline

n = int(input())
present = []

for _ in range(n):
    a = list(map(int, input().split()))

    # 아이들을 만난 경우
    if a[0] == 0:

        # 선물 없을 경우
        if len(present) == 0:
            print(-1)

        # 선물이 있는 경우
        else:
            print(max(present))
            present.remove(max(present))

    # 거점지에서 선물 추가
    else:
        for i in range(1, a[0]+1):
            present.append(a[i])