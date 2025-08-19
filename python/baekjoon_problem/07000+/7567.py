### 백준 7567 그릇
### 1초 이내


import sys
input = sys.stdin.readline

string = input().strip()

cnt = 10

for i in range(1, len(string)):
    if string[i-1] != string[i]:
        cnt += 10
    else:
        cnt += 5

print(cnt)