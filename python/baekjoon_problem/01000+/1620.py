### 백준 1620 나는야 포켓몬 마스터 이다솜
### 2초

### 그냥 풀었을 때 시간 초과 나서, 집합을 이용하여 시간 단축

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

dogam = []
dogam_dict = {}

for i in range(N):
    poketmon = input().strip()
    dogam.append(poketmon)
    dogam_dict[poketmon] = i + 1

ans = []

for _ in range(M):
    q = input().strip()
    ans.append(q)

for i in range(M):
    # 숫자일 경우
    if ans[i].isdigit():
        print(dogam[int(ans[i]) - 1])
    else:
        print(dogam_dict[ans[i]])