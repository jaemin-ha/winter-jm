### 백준 14626 ISBN
### 1초

ispn = input()
cnt = 0
position = -1

dict = {
    0: 0,
    1: 7,
    2: 4,
    3: 1,
    4: 8,
    5: 5,
    6: 2,
    7: 9,
    8: 6,
    9: 3,
    10: 0
}

for i in range(len(ispn)):
    if ispn[i] == '*':
        position = i
        continue
    if i % 2 == 0:
        cnt += int(ispn[i])
    else:
        cnt += int(ispn[i]) * 3

if position % 2 == 0:
    result = (10 - (cnt % 10)) % 10
    print(result)
else:
    result = 10 - (cnt % 10)
    print(dict[result])
