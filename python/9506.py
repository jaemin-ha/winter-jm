# 백준 9506 약수들의 합

import sys
input = sys.stdin.readline

while True:
    N = int(input())
    if N == -1:
        break

    # 약수 리스트
    lst = []

    # 약수 넣기 -> 출력값에 N은 뺴야하므로 N-1까지만
    for i in range(1, N):
        if N % i == 0:
            lst.append(i)

    # 결과
    result = ""

    # 완전수라면
    if sum(lst) == N:
        result += str(N)
        result += " = "
        # 첫번째 미리 추가
        result += str(lst[0])

        # 약수들 추가
        for i in range(1, len(lst)):
            result += " + "
            result += str(lst[i])
        print(result)

    else:
        print(f'{N} is NOT perfect.')