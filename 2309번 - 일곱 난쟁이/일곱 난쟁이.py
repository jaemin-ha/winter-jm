from itertools import combinations
import sys
input = sys.stdin.readline

# 주어진 키 배열
heights = []

for _ in range(9):
    num = int(input())
    heights.append(num)

# 조합 만들기
candidates = list(combinations(heights, 7))

for i in range(len(candidates)):
    if sum(candidates[i]) == 100:
        result = candidates[i]

for i in range(7):
    print(sorted(result)[i])