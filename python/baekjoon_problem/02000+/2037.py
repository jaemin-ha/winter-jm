### 백준 2037 문자메시지
##  2초 이내
##  딕셔너리로 구분 시킨 후, 계산 과정
##  1번에 못 맞춘 이유 
#   -> 처음에도 여러 번 누르는 게 가능 , 공백 입력시에는 대기시간 없음

# 같은 숫자 위에 있는 것들 구별
dict_1 = {
    'A': 2, 'B': 2, 'C': 2, 'D': 3, 'E': 3,
    'F': 3, 'G': 4, 'H': 4, 'I': 4, 'J': 5,
    'K': 5, 'L': 5, 'M': 6, 'N': 6, 'O': 6,
    'P': 7, 'Q': 7, 'R': 7, 'S': 7, 'T': 8,
    'U': 8, 'V': 8, 'W': 9, 'X': 9, 'Y': 9,
    'Z': 9, ' ': 1
}

# 누르는 횟수에 따라 달라지는 경우
dict_2 = {
    'A': 1, 'B': 2, 'C': 3, 'D': 1, 'E': 2,
    'F': 3, 'G': 1, 'H': 2, 'I': 3, 'J': 1,
    'K': 2, 'L': 3, 'M': 1, 'N': 2, 'O': 3,
    'P': 1, 'Q': 2, 'R': 3, 'S': 4, 'T': 1,
    'U': 2, 'V': 3, 'W': 1, 'X': 2, 'Y': 3,
    'Z': 4, ' ': 1
}

import sys

p, w = map(int, sys.stdin.readline().split())

string = list(sys.stdin.readline().strip())

# 처음 것 먼저 추가
cnt = p * (dict_2[string[0]])

# 맨 처음 다음 것 부터 계산
for i in range(1, len(string)):
    # 같을 경우
    if dict_1[string[i-1]] == dict_1[string[i]]:
        # 공백은 대기시간 없음
        if string[i] == ' ':
            cnt += p * dict_2[string[i]]
        else:
            cnt += (p * dict_2[string[i]]) + w
            
    # 다를 경우
    else:
        cnt += p * dict_2[string[i]]

print(cnt)