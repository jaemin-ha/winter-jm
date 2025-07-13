### 백준 29790 임스의 메이플컵
##  0.1초 이내

import sys

N, U, L = map(int, sys.stdin.readline().split())

condition1 = 0
condition2 = 0

if N >= 1000:
    condition1 = 1

if U >= 8000 or L >= 260:
    condition2 = 1

if condition1 == 1 and condition2 == 1:
    print("Very Good")
elif condition1 == 1 and condition2 != 1:
    print("Good")
else:
    print("Bad")