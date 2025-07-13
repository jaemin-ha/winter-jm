# 백준 1920 수 찾기
# 1초 이내

import sys

N = int(sys.stdin.readline())

# 주어진 숫자 배열
# set을 사용하면, O(1)로 줄어들음, list는 O(N)
nums = set(map(int, sys.stdin.readline().split()))

M = int(input())

# 찾을 숫자들
searches = list(map(int, sys.stdin.readline().split()))

for i in searches:
    print(1 if i in nums else 0)