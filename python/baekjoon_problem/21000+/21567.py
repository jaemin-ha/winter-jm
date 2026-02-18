# 백준 21567 숫자의 개수 2

lst = [0] * 10

A = int(input())
B = int(input())
C = int(input())

D = str(A * B * C)

for i in D:
    lst[int(i)] += 1

for j in range(10):
    print(lst[j])