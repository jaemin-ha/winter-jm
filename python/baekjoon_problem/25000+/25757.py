### 백준 25757 임스와 함께하는 미니게임
##  1초

import sys

N, game = sys.stdin.readline().split()

# 참가자 정리
participate = set()

for _ in range(int(N)):
    people = sys.stdin.readline().strip()
    participate.add(people)

result = 0

# 게임 종류에 따른 분류
if game == 'Y':
    result = len(participate)
elif game == 'F':
    result = len(participate) // 2
else:
    result = len(participate) // 3


print(result)
