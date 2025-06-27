def dfs(start, end):
    # 리프 노드까지 내려옴
    if start == end:
        return

    # 구간을 반반씩 탐색
    mid = (start + end) // 2

    # 왼쪽
    dfs(start, mid)

    # 오른쪽
    dfs(mid + 1, end)

    print(f'{start} ~ {end}')

dfs(1, 8)