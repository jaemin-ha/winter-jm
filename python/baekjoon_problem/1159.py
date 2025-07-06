### 백준 1159 농구 경기
##  1초

import sys

# 선수 숫자
N = int(sys.stdin.readline())

# 알파벳
lst = [0] * 26

# 선수 추가
for i in range(N):
    player = sys.stdin.readline()
    lst[ord(player[0])-97] += 1

# 결과값 담을 리스트
result = []

for i in range(26):
    if lst[i] >= 5:
        result.append(chr(i+97))

# 출력
if len(result) == 0:
    print('PREDAJA')
else:
    print(''.join(result))