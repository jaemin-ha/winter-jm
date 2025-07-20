### 백준 1874 스택 수열
##  2초

##  25.07.20.13시 -> 30분 고민했는데 못 품
##  풀이 참고 해서 작성

N = int(input())

# +, - 넣을 리스트
result = []

stack = [0] * 100000
top = -1

# 가능, 불가능 판단
ans = 1

# 1부터 시작
now = 1

for _ in range(N):
    num = int(input())
    # 1부터 스택에 비교
    # 작다면 스택에 push
    while now <= num:
        top += 1
        stack[top] = now
        result.append('+')
        now += 1

    # top에 있는 거랑 num이랑 같으면
    # pop
    if stack[top] == num:
        top -= 1
        result.append('-')

    # 다르면 불가능한 경우
    else:
        ans = 0

# 출력
if ans == 0:
    print('NO')

else:
    for i in result:
        print(i)