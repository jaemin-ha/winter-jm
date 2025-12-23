# 백준 18870 좌표 압축
# 단순 압축은 시간 초과 -> 딕셔너리를 이용하기
# 중복 제거 후 정렬하면 그 인덱스가 그 숫자보다 작은 것들의 수를 나타냄

import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

# 중복 제거, 정렬
new_num = sorted(set(nums))

# 딕셔너리에 입력
dict = {}
for i in range(len(new_num)):
    dict[new_num[i]] = i

# 출력
for s in nums:
    print(dict[s], end=" ")