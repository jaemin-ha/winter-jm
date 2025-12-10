# 백준 2948 2009년
dict = {1 : 31,
        2 : 28,
        3 : 31,
        4 : 30,
        5 : 31,
        6 : 30,
        7 : 31,
        8 : 31,
        9 : 30,
        10 : 31,
        11 : 30,
        12 : 31,}

# 날짜
D, M = map(int, input().split())

# 날짜를 숫자로 바꿈
result = 0

for i in range(1, M):
    result += dict[i]

result += D

if result % 7 == 0:
    print("Wednesday")

elif result % 7 == 1:
    print("Thursday")

elif result % 7 == 2:
    print("Friday")

elif result % 7 == 3:
    print("Saturday")

elif result % 7 == 4:
    print("Sunday")

elif result % 7 == 5:
    print("Monday")

elif result % 7 == 6:
    print("Tuesday")