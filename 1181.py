# 백준 1181 단어 정렬

import sys
input = sys.stdin.readline

N = int(input())
# 길이가 50까지
word_lst = [[] for _ in range(51)]

for _ in range(N):
    word = input().strip()
    # 중복 방지
    if word in word_lst[len(word)]:
        continue
    # 추가
    word_lst[len(word)].append(word)

# 정렬
for i in range(1, 51):
    word_lst[i].sort()

# 출력
for i in range(1, 51):
    for j in range(len(word_lst[i])):
        print(word_lst[i][j])