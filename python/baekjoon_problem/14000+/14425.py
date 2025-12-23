# 백준 14425 문자열 집합

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = set()
cnt = 0

for _ in range(N):
    string1 = input().strip()
    lst.add(string1)

for _ in range(M):
    string2 = input().strip()
    if string2 in lst:
        cnt += 1

print(cnt)