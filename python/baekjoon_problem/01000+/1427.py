# 백준 1427 소트인사이드
# join은 문자열에서만 가능

import sys
input = sys.stdin.readline

num = input().strip()
# 카운팅 정렬 이용
cnt = [0] * 10
result = []

# 개수 세기
for i in range(len(num)):
    cnt[int(num[i])] += 1

# 반대로 추가
for i in range(9, -1, -1):
    if cnt[i]:
        for _ in range(cnt[i]):
            result.append(str(i))

print(''.join(result))