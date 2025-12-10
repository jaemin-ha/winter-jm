# 백준 9063 대지

N = int(input())

x_lst = []
y_lst = []

# N = 1이면 사각형을 만들 수 없음
if N < 2:
    print(0)

else:
    for i in range(N):
        x, y = map(int, input().split())
        x_lst.append(x)
        y_lst.append(y)

    x_length = max(x_lst) - min(x_lst)
    y_length = max(y_lst) - min(y_lst)

    print(x_length * y_length)