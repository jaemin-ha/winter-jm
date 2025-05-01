T = int(input())

for tc in range(T):
    txt = input()

    top = -1
    stack = [0] * 51

    # 처음에 된다고 가정
    ans = 1

    # 순회
    for x in txt:
        if x == '(':
            top += 1
            stack[top] = '('
        
        # 닫는 괄호일 경우
        elif x == ')':
            # top = -1 -> 비어있으면 불가능
            if top == -1:
                ans = 0
                break
            # 아니라면 진행
            else:
                top -= 1
                stack[top+1] = 0
    
    # 스택에 남아있다면
    if top > -1:
        ans = 0
    

    # 결과값 출력
    if ans == 1:
        print('YES')
    else:
        print('NO')