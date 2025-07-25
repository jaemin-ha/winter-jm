### 백준 2493 탑  -> 오큰수랑 똑같은 문제
### 1.5초

import sys

input = sys.stdin.readline

N = int(input())
tops = list(map(int, input().split()))

new_tops = tops[::-1]

result = [0] * N
stack = []

# # 완전 탐색
# for i in range(N):
#     for j in range(i, N):
#         if new_tops[i] < new_tops[j]:
#             result.append(N-j)
#             break
#     else:
#         result.append(0)


# print(*result[::-1])


for i in range(N):
    while stack and new_tops[stack[-1]] < new_tops[i]:
        index = stack.pop()

        result[index] = N-i

    stack.append(i)

print(*result[::-1])
