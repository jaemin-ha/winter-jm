### 백준 Strfry
### 2초 이내

## 아이디어 : 문자열 정렬 후 비교하면 될 것 같다고 생각


import sys

T = int(sys.stdin.readline())

for _ in range(T):
    str1, str2 = sys.stdin.readline().split()
    
    # 비교
    if sorted(str1) == sorted(str2):
        print("Possible")

    else:
        print("Impossible")