# 백준 2164 카드2
# deque 쓰는 건데 규칙 찾아서 품
N = int(input())

# 2로 나눠서 계산해야 하므로 2로 나눈 횟수를 구하는 함수
def two_divison(k, cnt):
    if k > 1:
        return two_divison(k // 2, cnt + 1)

    return cnt

a = two_divison(N, 0)

b = 2**a

c = N - b

# 0이면 그 자신 출력
if c == 0:
    print(b)
else:
    print(c*2)