# 백준 17286 유미

import math

def cal(x, y):
    # 거리를 이동하는 건 좌표 차이가 아니라 대각선도 가능
    result = math.sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2)
    return result

yuumi = list(map(float, input().split()))
A = list(map(float, input().split()))
B = list(map(float, input().split()))
C = list(map(float, input().split()))

# 좌표가 유미 포함 4개여서
ans = min(
    cal(yuumi, A) + cal(A, B) + cal(B, C),
    cal(yuumi, A) + cal(A, C) + cal(C, B),
    cal(yuumi, B) + cal(B, A) + cal(A, C),
    cal(yuumi, B) + cal(B, C) + cal(C, A),
    cal(yuumi, C) + cal(C, A) + cal(A, B),
    cal(yuumi, C) + cal(C, B) + cal(B, A)
)

print(math.floor(ans))