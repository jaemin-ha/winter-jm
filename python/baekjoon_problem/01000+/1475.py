# 백준 1475 방 번호

from math import ceil

N = input()

# 개수 저장
COUNT = [0] * 10

# 개수 세기
for i in N:
    COUNT[int(i)] += 1

# 6과 9의 개수
cnt = 0

# 나머지 숫자 중 최대값
max_v = 0

for j in range(10):
    if j == 6 or j == 9:
        cnt += COUNT[j]
    else:
        if max_v < COUNT[j]:
            max_v = COUNT[j]

# cnt랑 max_v 비교해서 결과값 출력
if ceil(cnt / 2) >= max_v:
    result = ceil(cnt / 2)
else:
    result = max_v

print(result)