T = int(input())
 
for tc in range(1, T+1):
    N, Q = map(int, input().split())
 
    # 상자 배열 생성
    box_list = [0] * (N + 1)
 
    # 작업 수행
    for i in range(1, Q+1):
        L, R = map(int, input().split())
 
        for j in range(L, R+1):
            box_list[j] = i
 
    result = box_list[1:]
 
    print(f'#{tc}', *result)