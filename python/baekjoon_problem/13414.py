# 백준 13414 수강신청

import sys

K, M = map(int, input().split())

daegi = {}

for i in range(M):
    num = sys.stdin.readline().strip()
    daegi[num] = i

# 딕셔너리를 이용해서 튜플 만들고 튜플의 1값을 기준으로 정리
result = sorted(daegi.items(), key=lambda x:x[1])

# 수강 제한 보다 신청자 수가 적다면
if K > len(result):
    K = len(result)

for i in range(K):
    print(result[i][0])