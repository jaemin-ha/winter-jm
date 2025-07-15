### 백준 33556 Java String Equals
##  1초

A = input()
B = input()

# A가 null 이면 에러 발생
if A == 'null':
    print('NullPointerException')
    print('NullPointerException')
else:
    # A가 null이 아닌데 B가 null 이면 false 2개
    # 이거를 안할경우 A가 NULL B가 null일때 true가 나옴
    if B == 'null':
        print('false')
        print('false')
    else:
        # 대소문자 구분으로 같은 경우
        if A == B:
            print('true')
        else:
            print('false')

        # 모두 소문자로 만들어서 비교 -> 대, 소문자 구분 X
        if A.lower() == B.lower():
            print('true')
        else:
            print('false')
