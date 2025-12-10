import sys
input = sys.stdin.readline

N, M = map(int, input().split())
password = {}

for _ in range(N):
    info = list(input().split())
    password[info[0]] = info[1]

for _ in range(M):
    # \n 제거
    site = input().strip()
    print(password[site])