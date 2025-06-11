K = int(input())

top = -1
stack = [0] * 100000

for _ in range(K):
    num = int(input())

    if num == 0:
        top -= 1
        stack[top+1] = 0

    else:
        top += 1
        stack[top] = num

print(sum(stack))