# 백준 11653 소인수분해
# N이 1000만이라 시간초과날 줄 알았는데 그냥 통과됨

N = int(input())

lst = []

while N != 1:
    for i in range(2, N+1):
        if N % i == 0:
            lst.append(i)
            N //= i
            break

for num in lst:
    print(num)