### 백준 26068 치킨댄스를 추는 곰곰이를 본 임스 2
##  1초

import sys

N = int(input())

result = 0

for _ in range(N):
    D_date = input()
    
    # 날짜만 추출하기
    date = int(D_date[2:])

    if date <= 90:
        result += 1

print(result)