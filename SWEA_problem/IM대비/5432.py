T = int(input())

for tc in range(1, T+1):
    # 주어진 괄호 배열
    text = input()
    # 열린 괄호 개수
    cnt = 0
    # 조각 수
    result = 0

    for i in range(len(text)):
        c = text[i]

        if c == '(':
            cnt += 1

        elif c == ')':
            cnt -= 1

            # 여는 괄호 -> 그동안 쌓인 막대기 수
            # 이전 문자가 여는 괄호 => 레이저
            if text[i-1] == '(':
                # 그동안 쌓인 막대기만큼 조각 발생
                result += cnt

            # 이전 문자가 닫는 괄호 => 순수하게 막대기의 끝
            elif text[i-1] == ')':
                # 하나의 막대가 끝나서 한 조각만 증가
                result += 1

    print(f'#{tc} {result}')