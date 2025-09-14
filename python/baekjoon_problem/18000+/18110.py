### 백준 18110 solved.ac
### 파이썬 round는 반올림이랑 다른 듯

### -> .5일떄 무조건 올림하지 않고, 가장 가까운 짝수 정수로 반올림


import sys
input = sys.stdin.readline

def iround(x: float) -> int:
    # 0.5 이상은 무조건 올림하는 반올림 (양수 전제)
    return int(x + 0.5)

N = int(input())

lst = []

for _ in range(N):
    num = int(input())
    lst.append(num)

if N == 0:
    print(0)
else:
    lst.sort()
    k = iround((N / 100) * 15)

    cnt = 0
    for i in range(k, N-k):
        cnt += lst[i]

    print(iround(cnt / (N - k - k)))