# 모범 풀이 겸 복습

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    # 끝자리 N개가 모두 1인 수 -> 즉 ON이 되는 경우
    lastbinary = (1 << N) - 1

    # ON이 되는 경우와 M과 ON인 경우 &연산한 결과가 같으면 ON 상태
    if lastbinary == (M & lastbinary):
        print(f'#{tc} ON')
    else:
        print(f'#{tc} OFF')