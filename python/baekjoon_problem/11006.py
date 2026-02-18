# 백준 11006 남욱이의 닭장

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())

    # i : 멀쩡한 닭, j: 1개인 닭, 방정식 이용
    i = N - M
    j = 2*M - N

    print(j, i)