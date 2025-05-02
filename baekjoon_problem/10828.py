###  sys.stdin.readline()을 쓰자 -> 아니면 시간초과

import sys

n = int(input())

top = -1
stack = [0] * 10000

for _ in range(n):
    order = list(sys.stdin.readline().split())
    if order[0] == 'push':
        top += 1
        stack[top] = order[1]

    elif order[0] == 'pop':
        if top == -1:
            print(-1)
        else:
            top -= 1
            print(stack[top+1])

    elif order[0] == 'size':
        print(top+1)

    elif order[0] == 'empty':
        if top == -1:
            print(1)
        else:
            print(0)

    else:
        if top == -1:
            print(-1)
        else:
            print(stack[top])