# 실제 스스로 푼 풀이

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # 0부터 9까지 카운팅할 배열
    COUNT = [0] * 10
    
    # 양 세는 횟수
    cnt = 1

    # 합이 10보다 작을 때 -> 아직 모든 숫자가 안 나올 때
    while sum(COUNT) < 10:
        # 곱하는 과정 (N, 2N, 3N, ...)
        new_N = N * cnt

        nums = str(new_N)
        
        # 순회하면서 0일 경우 1추가
        for i in nums:
            if COUNT[int(i)] == 0:
                COUNT[int(i)] += 1
        
        # 횟수 증가
        cnt += 1
    
    print(f'#{tc} {(cnt-1) * N}')