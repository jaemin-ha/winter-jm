### 백준 14568 2017 연세대학교 프로그래밍 경시대회
##  1초 이내

N = int(input())

result = 0

# 1부터 사탕 개수까지
for i in range(1, N+1):
    for j in range(1, N+1):
        if j < i + 2:
            continue

        # 짝수이므로 2부터 시작
        for k in range(2, N+1, 2):
            # 사탕 개수 초과하면 넘김
            if i + j + k > N:
                break
            # 같으면 증가
            elif i + j + k == N:
                result += 1

print(result)