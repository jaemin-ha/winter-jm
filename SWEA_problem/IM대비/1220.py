T = 10

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 교착상태 수
    result = 0
    
    # 세로 방향이므로
    for c in range(N):
        # 교착 상태 전제 -> 1, 2순으로 와야함
        # state : 1이 나오면 state = 1로 바꿈
        state = 0
        for r in range(N):
            # 1이면 state 변화
            if arr[r][c] == 1:
                state = 1
            
            # state가 1이고 arr[r][c]가 2이면 result 1 증가
            if state == 1 and arr[r][c] == 2:
                result += 1
                # 다시 상태 초기화
                state = 0

    print(f'#{tc} {result}')