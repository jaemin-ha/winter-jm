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

    # 정류장 수
    P = int(input())

    # 결과
    bus_stop = []
    for i in range(P):
        C = int(input())
        bus_stop.append(bus[C])

    print(f'#{tc}', *bus_stop)
