# 백준 34183 SUPAC 의자 준비하기

# N : 팀 수, M: 가지고 있는 의자 개수
N, M, A, B = map(int, input().split())

need_chair = N * 3

if M >= need_chair:
    print(0)

else:
    print((need_chair - M) * A + B)