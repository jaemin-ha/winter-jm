T = 10

for tc in range(1, T+1):
    N = int(input())
    array = [list(map(int, input().split())) for _ in range(100)]
    
    max_v = -float('inf')
    
    # 가로
    for i in range(100):
        s = 0
        for j in range(100):
            s += array[i][j]
            if max_v < s:
                max_v = s
    

    # 세로
    for j in range(100):
        s = 0
        for i in range(100):
            s += array[i][j]
            if max_v < s:
                max_v = s

    # 대각선
    # \
    s = 0
    for i in range(100):
        s += array[i][i]
        if max_v < s:
            max_v = s
    
    # /
    s = 0
    for i in range(100):
        s += array[i][99-i]
        if max_v < s:
            max_v = s
    

    print(f'#{tc} {max_v}')