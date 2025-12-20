# 백준 14670 병약한 영정

import sys
input = sys.stdin.readline

# 약 개수
N = int(input())

# 약 담을 딕셔너리
dict = {}

for _ in range(N):
    effect, medicine = map(int, input().split())
    dict[effect] = medicine

# 증상 개수
R = int(input())

for _ in range(R):
    symptom = list(map(int, input().split()))
    symptom_num = symptom[0]

    result = []

    for i in range(1, symptom_num+1):
        if symptom[i] in dict:
            result.append(dict[symptom[i]])

    if len(result) == symptom_num:
        print(*result)

    else:
        print("YOU DIED")
