T = int(input())

# 단조 확인
def danjo(num):
    str_num = str(num)
    for i in range(len(str_num)-1):
        if str_num[i] > str_num[i+1]:
            return False
    return True

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    result = -1
    for i in range(N):
        for j in range(i+1, N):
            num = arr[i]*arr[j]
            if danjo(num):
                result = max(result, num)

    print(f'#{tc} {result}')