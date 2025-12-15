# 백준 2587 대표값2

lst = []

for _ in range(5):
    num = int(input())
    lst.append(num)

lst.sort()

print(sum(lst) // 5)
print(lst[2])