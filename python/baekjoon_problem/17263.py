# 백준 17263 Sort 마스터 배지훈

N = int(input())
nums = list(map(int, input().split()))

nums.sort()

print(nums[-1])