### 백준 6750 Rotating letters


lst = ['I', 'O', 'S', 'H', 'Z', 'X', 'N']

string = input()

cnt = 0

for i in string:
    if i in lst:
        cnt += 1

if cnt == len(string):
    print('YES')
else:
    print('NO')