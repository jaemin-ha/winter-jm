### 백준 1864 문어 숫자
##  1초 이내
##  딕셔너리 이용해서 계산해야한다고 생각함


# 숫자로 변환할 딕셔너리
dict = {'-' : 0,
        '\\' : 1,
        '(' : 2,
        '@' : 3,
        '?' : 4,
        '>' : 5,
        '&' : 6,
        '%' : 7,
        '/' : -1
        }

while True:
    string = input()
    # #이면 종료
    if string == '#':
        break
    else:
        # 계산 결과 값
        cnt = 0
        # 뒤에서부터 계산
        for i in range(len(string)-1, -1, -1):
            cnt += dict[string[i]] * (8**(len(string) - 1 - i))

    print(cnt)