### 백준 1919 애너그램 만들기
## 2초 이내

## 교집합을 이용해서 구하려고 했으나
## 예외가 존재 -> 답은 2인데, 출력값이 2로 나옴
'''
aab
abb
'''

## 카운팅한 후 구하는 방법으로 선회

import sys

first = sys.stdin.readline().strip()
second = sys.stdin.readline().strip()

# 카운팅 배열
first_cnt = [0] * 26
second_cnt = [0] * 26

for alphabet in first:
    first_cnt[ord(alphabet) - 97] += 1

for alphabet in second:
    second_cnt[ord(alphabet) - 97] += 1


result = 0

# 삭제 문자 구하기
for i in range(26):
    result += abs(first_cnt[i] - second_cnt[i])

print(result)