### 백준 1264 모음의 개수
## 1초 이내 -> 파이썬 1억번 연산
## 문자열 입력받고, 그 안에서 모음 찾으면 된다고 생각

import sys

# set으로 최적화
moeum = {"A", "E", "I", "O", "U", "a", "e", "i", "o", "u"}

while True:
    string = sys.stdin.readline().strip()
    # 결과값
    cnt = 0

    # 종료 조건
    if string == "#":
        break
    
    # 모음 찾기
    for char in string:
        if char in moeum:
            cnt += 1

    print(cnt)