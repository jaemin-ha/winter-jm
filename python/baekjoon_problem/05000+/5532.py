### 방학 숙제

import sys
from math import ceil

L = int(sys.stdin.readline())

A = int(sys.stdin.readline())

B = int(sys.stdin.readline())

C = int(sys.stdin.readline())

D = int(sys.stdin.readline())

print(L - max(ceil(A / C), ceil(B / D )))