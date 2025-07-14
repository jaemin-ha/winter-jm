### 백준 28455 Union Maplestory
##  1초

N = int(input())

level_lst = []

level_sum = 0

status = 0

for _ in range(N):
    level = int(input())

    level_lst.append(level)

level_lst.sort(reverse=True)

if N >= 42:
    for i in range(42):
        level_sum += level_lst[i]
        if level_lst[i] >= 250:
            status += 5
        elif 200 <= level_lst[i] < 250:
            status += 4
        elif 140 <= level_lst[i] < 200:
            status += 3
        elif 100 <= level_lst[i] < 140:
            status += 2
        elif 60 <= level_lst[i] < 100:
            status += 1
else:
    for i in range(N):
        level_sum += level_lst[i]
        if level_lst[i] >= 250:
            status += 5
        elif 200 <= level_lst[i] < 250:
            status += 4
        elif 140 <= level_lst[i] < 200:
            status += 3
        elif 100 <= level_lst[i] < 140:
            status += 2
        elif 60 <= level_lst[i] < 100:
            status += 1


print(level_sum, status)