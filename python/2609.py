# 백준 2609 최대공약수와 최소공배수

import sys
input = sys.stdin.readline

# 두 개의 자연수
nums = list(map(int, input().split()))

# 임시 값
a = 0

# 최대공약수
for i in range(1, min(nums) + 1):
    if (nums[0] % i == 0 and nums[1] % i == 0):
        a = i

# 최소공배수는 최대공약수로 나눈후 곱하면 구할 것이라고 생각함
b = a * (nums[0] // a) * (nums[1] // a)

print(a)
print(b)