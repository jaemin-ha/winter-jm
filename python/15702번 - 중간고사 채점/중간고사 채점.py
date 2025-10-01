### 동점일 경우 작은 번호 출력
### score를 첨에 -1로 해서 답이 -1이 나오는 과정이 있었음

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
problems = list(map(int, input().split()))

person = -1
ans_score = -1

for _ in range(M):
    score = 0
    info = list(input().split())

    for i in range(1, N+1):
        if info[i] == 'O':
            score += problems[i-1]
    
    # 클 경우
    if ans_score < score:
        person = int(info[0])
        ans_score = score

    # 같을 경우
    elif ans_score == score:
        if person > int(info[0]):
            person = int(info[0])
            ans_score = score

print(person, ans_score)