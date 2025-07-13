### 백준 2789 유학 금지
##  1초

## 밴 만들고, 밴에 존재하면 제거하는 방식으로 생각

ban = {'C', 'A', 'M', 'B', 'R', 'I', 'D', 'G', 'E'}

string = input()

result = []

for i in string:
    if i not in ban:
        result.append(i)

print(''.join(result))