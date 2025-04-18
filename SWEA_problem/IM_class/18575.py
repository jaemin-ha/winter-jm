T = int(input())

# 상하좌우
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

# 점수 계산하는 함수
def cnt_balloon(tr, tc, balloon_list, N):
    global max_v, min_v

    # 초기값 설정
    s = balloon_list[tr][tc]

    for d in range(4):
        for k in range(1, N):
            nr = tr + dr[d] * k
            nc = tc + dc[d] * k

            # 범위 확인
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue
            
            s += balloon_list[nr][nc]

    # 최대
    if max_v < s:
        max_v = s
    
    # 최소
    if min_v > s:
        min_v = s



for tc in range(1, T+1):
    N = int(input())
    balloon_list = [list(map(int, input().split())) for _ in range(N)]
    
    # 최대값, 최소값값
    max_v = - float('inf')
    min_v = float('inf')

    # 모든 경우 생각하기
    for r in range(N):
        for c in range(N):
            cnt_balloon(r, c, balloon_list, N)


    print(f'#{tc} {max_v-min_v}')
