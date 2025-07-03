### 백준 2520 팬케이크 사랑
##  1초

import sys
from math import floor

T = int(input())

for tc in range(1, T+1):
    # 빈 줄 없애기
    gonbaek = sys.stdin.readline()

    # 입력 받기
    banjuk = list(map(int, sys.stdin.readline().split()))
    jaerou = list(map(int, sys.stdin.readline().split()))

    # 만들 수 있는 반죽 구하기
    banjuk1 = banjuk[0] / 8
    banjuk2 = banjuk[1] / 8
    banjuk3 = banjuk[2] / 4
    banjuk4 = banjuk[3] / 1
    banjuk5 = banjuk[4] / 9

    # 그 중 최소값 (버림)
    make_banjuk = floor(16 * min(banjuk1, banjuk2, banjuk3, banjuk4, banjuk5))

    # 만들 수 있는 재료 구하기
    jaerou1 = jaerou[0] // 1
    jaerou2 = jaerou[1] // 30
    jaerou3 = jaerou[2] // 25
    jaerou4 = jaerou[3] // 10

    # 합이 만들 수 있는 재료
    make_jaerou = jaerou1 + jaerou2 + jaerou3 + jaerou4

    # 그 중 최소값이 정답
    result = min(make_banjuk, make_jaerou)

    print(result)