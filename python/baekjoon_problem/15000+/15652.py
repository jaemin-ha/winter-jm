### 백준 15652 N과 M (4)
### 오름차순으로

import sys

input = sys.stdin.readline()

N, M = map(int, input.split())

arr = [0] * M


def check(depth):
    # 깊이가 1면 True 반환
    if depth == 0:
        return True

    # 내림차순인지 확인
    if arr[depth-1] <= arr[depth]:
        return True
    else:
        return False

def recur(depth):
    if depth == M:
        print(*arr)
        return
    
    for i in range(1, N+1):
        arr[depth] = i
        # 체크 확인
        if check(depth):
            recur(depth+1)

recur(0)