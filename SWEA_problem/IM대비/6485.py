T = int(input())

for tc in range(1, T+1):
    # 노선 개수
    N = int(input())

    # 정류장 지나는 숫자 세기위한 리스트
    bus = [0] * 5001

    for _ in range(N):
        A, B = map(int, input().split())

        for i in range(A, B+1):
            bus[i] += 1

    # 출력할 정류장 수
    P = int(input())
    
    # 정류장 추가할 리스트
    bus_stop = []
    for _ in range(P):
        C = int(input())
        bus_stop.append(C)

    # 정답
    result = []
    for i in range(P):
        result.append(bus[bus_stop[i]])

    print(f'#{tc}', *result)
