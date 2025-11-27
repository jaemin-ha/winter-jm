import sys
input = sys.stdin.readline

i = 0

while True:
    L, P, V = map(int, input().split())
    
    if V == 0:
        break
    
    i += 1
    s1 = V // P

    K = L * s1

    s2 = min(V % P, L)

    print(f'Case {i}: {K + s2}')
