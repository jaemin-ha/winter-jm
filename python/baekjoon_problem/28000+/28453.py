### 백준 28453 Previous Level
##  1초


N = int(input())

levels = list(map(int, input().split()))

result = []

for i in range(N):
    if levels[i] == 300:
        result.append(1)
    elif 275 <= levels[i] < 300:
        result.append(2)
    elif 250 <= levels[i] < 275:
        result.append(3)
    else:
        result.append(4)

print(*result)