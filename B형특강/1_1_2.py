# 모범 풀이 -> 비트 연산

T = int(input())

# 10번 쉬프트하고 -1 하면 01111111111 -> 9부터 0까지 셀 수 있음
total = (1 << 10) - 1

for tc in range(1, T+1):
    N = int(input())

    # 모두 0인 visited
    visited = 0

    # 세는 횟수
    cnt = 0

    while True:
        cnt += 1
        new_N = str(N * cnt)

        for c in new_N:
            num = int(c)
            # OR 연산을 통해 num번째 비트를 켜는 방식
            visited |= (1 << num)
        
        # 같으면 종료
        if visited == total:
            break
    
    print(f'#{tc} {N * cnt}')