# 백준 10886 0 = not cute / 1 = cute

import sys
input = sys.stdin.readline

N = int(input())

agree = 0
disagree = 0

for _ in range(N):
    thinkness = int(input())

    if thinkness:
        agree += 1

    else:
        disagree += 1

if agree > disagree:
    print("Junhee is cute!")

else:
    print("Junhee is not cute!")