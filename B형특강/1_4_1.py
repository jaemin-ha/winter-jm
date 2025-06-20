# 실제 스스로 푼 풀이  -> 채점은 못 해봤지만 맞을 것으로 추정

T = int(input())

for tc in range(1, T+1):

    # N 자연수 개수, M 명령 수, L 최종 출력 인덱스
    N, M, L = map(int, input().split())

    # 배열
    nums = list(map(int, input().split()))

    for _ in range(M):
        order = list(input().split())

        # I면 특정 인덱스 자리에 추가
        if order[0] == 'I':
            nums.insert(int(order[1]), int(order[2]))
        
        # D면 특정 인덱스 자리 삭제
        elif order[0] == 'D':
            del nums[int(order[1])]
        
        # C면 인덱스 자리 변경
        else:
            nums[int(order[1])] = int(order[2])

    try:
        print(f'#{tc} {nums[L]}')

    # 인덱스 값이 존재하지 않다면 -1 출력
    except:
        print(f'#{tc} -1')