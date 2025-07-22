### 백준 17298 오큰 수
### 1초 이내

### 완전 탐색으로 풀었지만, 시간 초과로 인해 고민
### 고민해봤지만, 떠오르지 않아 풀이를 보고 이해함

import sys

N = int(sys.stdin.readline())

nums = list(map(int, sys.stdin.readline().split()))

# 기본값을 -1로 가정
result = [-1] * N

# 인덱스 넣을 스택
stack = []

for i in range(N):
    # 스택이 비어 있지 않고, 스택의 마지막 인덱스의 값보다 현재 인덱스의 값이 클 때
    # 이게 해당안되면 오큰수가 아니다
    while stack and nums[stack[-1]] < nums[i]:
        # 스택의 마지막 인덱스를 꺼냄
        index = stack.pop()

        # 결과값 갱신
        result[index] = nums[i]
    
    # 스택의 인덱스 값 추가
    stack.append(i)

print(*result)