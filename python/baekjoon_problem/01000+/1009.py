# 백준 1009 분산 처리

lst = [[10], [1], [2, 4, 8, 6], [3, 9, 7, 1], [4, 6],
       [5], [6], [7, 9, 3, 1], [8, 4, 2, 6], [9, 1]]


one_lst = ["1", "5", "6", "0"]
two_lst = ["4", "9"]

N = int(input())

for _ in range(N):
    num, gob = map(int, input().split())

    s = str(num)[-1]

    # 1가지 경우
    if s in one_lst:
        print(lst[int(s)][0])

    # 2가지 경우
    elif s in two_lst:

        if gob % 2 == 1:
            print(lst[int(s)][0])

        else:
            print(lst[int(s)][1])

    # 4가지 경우
    else:
        if gob % 4 == 1:
            print(lst[int(s)][0])

        elif gob % 4 == 2:
            print(lst[int(s)][1])

        elif gob % 4 == 3:
            print(lst[int(s)][2])

        else:
            print(lst[int(s)][3])
