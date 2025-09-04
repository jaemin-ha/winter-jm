N, M = map(int, input().split())

a = set()
b = set()

for _ in range(N):
    name = input()
    a.add(name)

for _ in range(M):
    name = input()
    b.add(name)

c = a & b
new_c = sorted(list(c))

print(len(c))

for i in range(len(new_c)):
    print(new_c[i])