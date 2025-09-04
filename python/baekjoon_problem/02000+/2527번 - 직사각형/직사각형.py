'''
3 10 50 60 100 100 200 300
45 50 600 600 400 450 500 543
11 120 120 230 50 40 60 440
35 56 67 90 67 80 500 600
'''

import sys
input = sys.stdin.readline

for _ in range(4):
    board = [[0] * 1001 for _ in range(1001)]
    square = list(map(int, input().split()))

    for r in range(square[0], square[2] + 1):
        for c in range(square[1], square[3] + 1):
            board[r][c] += 1

    for r in range(square[4], square[6] + 1):
        for c in range(square[5], square[7] + 1):
            board[r][c] += 1
    cnt = 0
    for r in range(1001):
        for c in range(1001):
            if board[r][c] == 2:
                cnt += 1
    
    if cnt == 0:
        print('d')
    elif cnt == 1:
        print('c')
    else:
        print('a')