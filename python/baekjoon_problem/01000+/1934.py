# 백준 1934 최소공배수

import sys
input = sys.stdin.readline

T = int(input())

for tc in range(T):
    A, B = map(int, input().split())
    result = 0
    
    # 최대 공약수
    for i in range(1, 45001):
        if A % i == 0 and B % i == 0:
            result = i

    a = A // result
    b = B // result
    
    # 최소 공배수
    print(a * b * result)