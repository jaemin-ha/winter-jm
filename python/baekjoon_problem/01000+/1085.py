### 직사각형에서 탈출
##  2초 이내
##  아이디어: (0,0) , (w, h) 가지고 거리의 최소값 구하기

import sys

x, y, w, h = map(int, sys.stdin.readline().split())

W = abs(w - x)
H = abs(h - y)

print(min(x, y, W, H))