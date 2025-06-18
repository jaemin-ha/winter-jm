# 충전 횟수 찾기
def count_charge(K, N, bus_charges):
    current = 0
    cnt = 0

    # 도착할 때 까지
    while current < N:
        # 가능한 충전소
        candidates = [c for c in bus_charges if c <= current + K and c > current]

        # 도착한다면 종료
        if current + K >= N:
            return cnt
        
        # 갈 충전소가 없다면 0 반환
        elif len(candidates) == 0:
            return 0
        
        # 그게 아니라면 갈 곳이 존재 이동 시키고 횟수 증가
        else:
            current = max(candidates)
            cnt += 1

T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    bus_charges = list(map(int, input().split()))
    result = count_charge(K, N, bus_charges)
    print(f'#{tc} {result}')