# 백준 9625 BABBA

K = int(input())

a = 1
b = 0

for i in range(K):
    pre_a = a

    # A는 이전 B개수와 동일, B는 A개수 추가
    a = b
    b += pre_a

print(a, b)