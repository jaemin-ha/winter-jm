### 백준 1406 에디터
##  0.3초 이내

#  첨에 스택 1개로 풀었음 -> 시간 복잡도 O(M * N) -> 시간 초과 발생
#  찾아보니 스택 2개로 푸는 방법이 존재 -> 시간 복잡도 O(M + N)으로 줄임
#  그러나 입력 방식이 느려서 sys 도입해서 풀음

import sys

# 스택을 2개 사용
left = list(sys.stdin.readline().strip())
right = []

N = int(sys.stdin.readline())

for _ in range(N):
    # 명령문
    order = sys.stdin.readline().split()

    # 커서 1개 왼쪽으로 옮김 -> 왼쪽 마지막을 pop해서 right에 추가
    if order[0] == 'L':
        if left:
            right.append(left.pop())

    # 커서 1개 오른쪽으로 옮김 -> 오른쪽을 pop해서 left에 추가
    elif order[0] == 'D':
        if right:
            left.append(right.pop())

    # 왼쪽 마지막 제거
    elif order[0] == 'B':
        if left:
            left.pop()

    # 추가
    elif order[0] == 'P':
        left.append(order[1])

# right는 거꾸로 쌓이기 때문에 뒤집음
result = ''.join(left + right[::-1])

print(result)