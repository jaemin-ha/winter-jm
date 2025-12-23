# 백준 1436 영화감독 숌
# 코드를 짜고 N = 1000해보니 2666799이길래 될 것 같음

# 이게 더 쉬운 풀이
# 666이 들어있는지 확인하는 듯 (개수 세지 않고)

# N = int(input())
# cnt = 0
# 
# i = 665
# while cnt < N:
#     if "666" in str(i):
#         cnt += 1
#     i += 1
# 
# print(i-1)

import sys
input = sys.stdin.readline

N = int(input())
six_lst = []

# 1번째가 666
s = 666
while len(six_lst) < 10000:
    cnt = 0
    # 수가 6이 연속으로 3개 들어갔는지 확인
    for num in str(s):
        if num == '6':
            cnt += 1

            #  연속으로 나온게 3개면 추가
            if cnt == 3:
                six_lst.append(s)
                break

        # 6이 아니면 0으로 초기화
        else:
            cnt = 0

    # 다음 수로 진행
    s += 1

print(six_lst[N-1])