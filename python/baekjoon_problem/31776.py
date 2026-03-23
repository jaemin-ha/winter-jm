# 백준 31776 예비 소집 결과 보고서

N = int(input())

result = 0

for _ in range(N):
    a, b, c = map(int, input().split())
    
    # 첫문째부터 해결이니까 첫 문제를 못 풀면 넘김
    if a == -1:
        continue

    else:
        # 두번째 못 풀면 무조건 세번쨰도 못풀어야함
        if b == -1:
            if c != -1:
                continue
            else:
                if c == -1:
                    result += 1

        else:
            # 크기 비교
            if b >= a:
                if c == -1:
                    result += 1
                else:
                    if c >= b:
                        result += 1

print(result)