import sys
input = sys.stdin.readline

N = int(input())

x_lst = []
y_lst = []

a = 0
b = 0

for _ in range(N):
    x, y = map(int, input().split())
    x_lst.append(x)
    y_lst.append(y)

for i in range(-1, N-1):
    a += x_lst[i] * y_lst[i+1]


for j in range(-1, N-1):
    b += y_lst[j] * x_lst[j+1]

result = abs(a-b) / 2

print(result)