T = int(input())

for tc in range(1, T+1):
    arr = list(map(int, input()))

    # 고용 사람 수
    result = 0

    # 현재 박수 치는 사람 수
    current = arr[0]

    for i in range(1, len(arr)):
        if current < i:
            result += 1
            current += 1
            
        current += arr[i]

    print(f'#{tc} {result}')