# 백준 20492 세금

N = int(input())

a = int(N * 0.78)
b = int(N * 0.8 + (N * 0.2 * 0.78))

print(a, b)