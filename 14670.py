# 백준 14670 병약한 영정

import sys
input = sys.stdin.readline

# 약 개수
N = int(input())

# 증상과 약 담을 딕셔너리
dict = {}

for _ in range(N):
    effect, medicine = map(int, input().split())
    dict[effect] = medicine

# 증상 개수
R = int(input())

for _ in range(R):
    symptom = list(map(int, input().split()))
    
    # 증상 개수
    symptom_num = symptom[0]

    # 결과
    result = []

    # 증상이 딕셔너리에 있으면 결과에 추가
    for i in range(1, symptom_num+1):
        if symptom[i] in dict:
            result.append(dict[symptom[i]])

    # 결과에 있는 약과 증상 개수가 같은지 비교
    if len(result) == symptom_num:
        print(*result)

    else:
        print("YOU DIED")
