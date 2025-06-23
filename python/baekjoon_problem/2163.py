### 초콜릿 자르기

## 판단하는 함수
def judge(N, M):

    # 길이가 1인 경우에만 조금 더 고려하기
    if N == 1:
        cnt = M - 1
    elif M == 1:
        cnt = N - 1
    
    # 그 외의 경우에는 이거 인듯
    else:
        cnt = (N * M) - 1

    return cnt

N, M = map(int, input().split())

result = judge(N, M)

print(result)