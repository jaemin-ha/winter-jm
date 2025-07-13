### 백준 30403 무지개 만들기
##  1초

N = int(input())

string = input()

result = 0

result2 = 0

# 판단
if 'R' in string:
    result += 1

if 'O' in string:
    result += 1

if 'Y' in string:
    result += 1

if 'G' in string:
    result += 1

if 'B' in string:
    result += 1

if 'I' in string:
    result += 1

if 'V' in string:
    result += 1

if 'r' in string:
    result2 += 1

if 'o' in string:
    result2 += 1

if 'y' in string:
    result2 += 1

if 'g' in string:
    result2 += 1

if 'b' in string:
    result2 += 1

if 'i' in string:
    result2 += 1

if 'v' in string:
    result2 += 1

# 출력
if result >= 7 and result2 >= 7:
    print('YeS')
elif result >= 7 and result2 < 7:
    print('YES')
elif result < 7 and result2 >= 7:
    print('yes')
else:
    print('NO!')