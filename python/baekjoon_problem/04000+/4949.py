### 백준 4949 균형잡힌 세상
##  1초

while True:
    string = input()
    # 종료 조건
    if string == '.':
        break

    stack = [0] * 100
    top = -1
    
    # 일단 맞다고 가정
    ans = 1

    for x in string:
        if x in '([':
            top += 1
            stack[top] = x

        elif x in ')]':
            if top == -1:
                ans = 0
                break

            else:
                if x in ')':
                    if stack[top] == '(':
                        top -= 1
                    else:
                        ans = 0
                        break

                elif x in ']':
                    if stack[top] == '[':
                        top -= 1
                    else:
                        ans = 0
                        break
    
    # 스택에 남아 있는 경우
    if top > -1:
        ans = 0

    # 출력
    if ans == 0:
        print('no')
    else:
        print('yes')