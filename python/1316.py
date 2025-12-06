# 백준 1316 그룹 단어 체커

import sys

input = sys.stdin.readline

N = int(input())

result = 0

for _ in range(N):
    # 알파벳 확인
    lst = [0] * 26

    # 그룹 단어 확인용
    s = 0

    # 단어
    word = input().strip()

    # 첫 알파벳
    lst[ord(word[0]) - 97] += 1


    # 2번째부터 확인
    for i in range(1, len(word)):

        # 같은 지
        if word[i - 1] == word[i]:
            s += 1

        # 다른 지
        else:
            # 이미 나온 적 있는지
            if lst[ord(word[i]) - 97] == 0:
                lst[ord(word[i]) - 97] += 1
                s += 1

            # 이미 나왔다면 중단
            else:
                break

    if s == len(word) - 1:
        result += 1

print(result)

