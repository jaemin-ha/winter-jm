### 백준 2473 세 용액
### 1초

### 하나 고정 시키고, 투 포인터 씀
### 파이썬은 초과, 파이파이로 하니까 통과됨

import sys
input = sys.stdin.readline

N = int(input())
solutions = list(map(int, input().split()))
solutions.sort()

min_v = float('inf')

# 1개를 고르고 시작, 3개 이므로 i가 맨 앞이므로 i를 N-3까지
for i in range(N-2):
    # i 다음부터 설정
    s = i + 1
    e = N - 1
    while s < e:
        ans = solutions[s] + solutions[e] + solutions[i]

        if min_v > abs(ans):
            min_v = abs(ans)
            min_1, min_2, min_3 = solutions[s], solutions[e], solutions[i]

        if ans == 0:
            break

        elif ans > 0:
            e -= 1
        
        else:
            s += 1

# 오름차순 출력
result = [min_1, min_2, min_3]
result.sort()

print(*result)