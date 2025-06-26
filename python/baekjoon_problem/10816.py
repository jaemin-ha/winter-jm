### 백준 10816 숫자 카드 2
## 1초 이내

## 일단 바로 떠오르는 방법인 카운팅 배열로 풀음

import sys

N = int(sys.stdin.readline())

cards = list(map(int, sys.stdin.readline().split()))


M = int(sys.stdin.readline())

nums = list(map(int, sys.stdin.readline().split()))

# 숫자가 -10,000,000 부터 10,000,000 이므로
# 카운팅 배열
COUNT = [0] * 20000001

for num in cards:
    COUNT[num + 10000000] += 1

result = []

for num in nums:
    result.append(COUNT[num + 10000000])

print(*result)