### 두 수의 합
### 1초 이내

### 투 포인터를 이용한 풀이

import sys

n = int(sys.stdin.readline())

nums = list(map(int, sys.stdin.readline().split()))

x = int(sys.stdin.readline())

# 투 포인터를 위해선 정렬이 필요함
nums.sort()

lft = 0
rgt = n -1

cnt = 0

while lft < rgt:

    current = nums[lft] + nums[rgt]

    # 같다면 카운트
    if current == x:
        cnt += 1
        lft += 1
        rgt -= 1

    # 작다면 앞을 당김
    elif current < x:
        lft += 1

    # 크다면 뒤를 당김
    else:
        rgt -= 1

print(cnt)