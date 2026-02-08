# 백준 5300 Fill the Rowboats!

N = int(input())
lst = []

for i in range(1, N+1):
    lst.append(i)
    if i % N == 0 or i % 6 == 0:
        lst.append("Go!")

print(*lst)