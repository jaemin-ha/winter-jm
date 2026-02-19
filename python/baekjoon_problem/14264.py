# 백준 14264 정육각형과 삼각형

import math

L = int(input())

# 삼각형 최대값 -> 그냥 평범한 대각선, 정삼각형 넓이 공식
print(math.sqrt(3) * (L**2) / 4)