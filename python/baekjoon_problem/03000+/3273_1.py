### 두 수의 합
### 1초 이내

### set을 이용한 풀이

import sys

n = int(sys.stdin.readline())

nums = set(map(int, sys.stdin.readline().split()))

x = int(sys.stdin.readline())

# 결과값
cnt = 0

# 안에 존재하는 지 파악
for num in nums:
    result = x - num
    if result in nums:
        cnt += 1

print(cnt // 2)