# 백준 10989 수 정렬하기 3

# 첨에 리스트에 넣어 구하려고 했으나 시간초과 및 메모리초과
# 메모리를 줄이기 위해 -> 카운팅 정렬을 사용해야한다.
# O(N + K) -> 입력 개수, 숫자 범위

import sys
input = sys.stdin.readline

N = int(input())
# 개수를 세는 리스트 (카운팅 정렬)
cnt = [0] * 10001

for _ in range(N):
    num = int(input())
    cnt[num] += 1

# 개수가 존재하면 출력
for i in range(1, 10001):
    if cnt[i]:
        for _ in range(cnt[i]):
            print(i)