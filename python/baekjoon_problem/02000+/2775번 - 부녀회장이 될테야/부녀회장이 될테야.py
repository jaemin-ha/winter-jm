import sys
input = sys.stdin.readline

T = int(input())

apart = [[0] * 15 for _ in range(15)]

# 0층은 미리 적어두기
apart[0] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

# 아파트 정보 입력(k, n이 14까지 있음)
for i in range(1, 15):
    for j in range(1, 15):
        # 3중 반복문 말고, 2중만 쓰고 규칙을 이용
        apart[i][j] = apart[i-1][j] + apart[i][j-1]

for tc in range(1, T+1):
    # k : 층 정보, n : 호수
    k = int(input())
    n = int(input())

    print(apart[k][n])