### 백준 1284 집 주소
##  1초이내

import sys

# 0과 1을 제외한 숫자들
lst = ['2', '3', '4', '5', '6', '7', '8', '9']

while True:
    N = int(sys.stdin.readline())
    
    # 0 들어오면 종료
    if N == 0:
        break

    else:
        cnt = 2
        for i in str(N):
            if i in lst:
                cnt += 3
            elif i == '1':
                cnt += 2
            else:
                cnt += 4
    
    # 숫자 너비 길이 추가
    cnt += len(str(N)) - 1

    print(cnt)