# 백준 20001 고무오리 디버깅

import sys
input = sys.stdin.readline

start = input().strip()
# 문제 수
problem = 0

while True:
    order = input().strip()

    # 판정
    if order == "고무오리 디버깅 끝":
        if problem == 0:
            print("고무오리야 사랑해")
            break
        else:
            print("힝구")
            break

    # 문제 풀이
    if problem == 0 and order == "고무오리":
        problem += 2

    elif problem > 0 and order == "고무오리":
        problem -= 1

    else:
        problem += 1