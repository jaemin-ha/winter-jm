### 백준 1259 팰린드롬 수
##  1초

import sys

while True:
    # /n을 없애기 위해 strip사용
    N = sys.stdin.readline().strip()

    if N == '0':
        break
    
    else:
        # 문자열 뒤집기
        if N == N[::-1]:
            print('yes')
        else:
            print('no')