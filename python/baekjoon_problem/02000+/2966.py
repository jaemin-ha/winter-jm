### 백준 2966 찍기
##  1초

# 찍는 순서
sangun = ['A', 'B', 'C', 'A', 'B', 'C'] * 17

changyoung = ['B', 'A', 'B', 'C'] * 26

hyunjin = ['C', 'C', 'A', 'A', 'B', 'B'] * 17


# 입력
N = int(input())

correct_answer = input()

cnt1 = 0
cnt2 = 0
cnt3 = 0

# 상근
for i in range(N):
    if correct_answer[i] == sangun[i]:
        cnt1 += 1

# 창영
for i in range(N):
    if correct_answer[i] == changyoung[i]:
        cnt2 += 1

# 현진
for i in range(N):
    if correct_answer[i] == hyunjin[i]:
        cnt3 += 1

result = max(cnt1, cnt2, cnt3)

# 출력
print(result)
if result == cnt1:
    print('Adrian')
if result == cnt2:
    print('Bruno')
if result == cnt3:
    print('Goran')