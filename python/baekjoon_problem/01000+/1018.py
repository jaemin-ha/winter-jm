### 백준 1018 체스판 다시 칠하기
## 2초 이내
## 8 X 8 배열 만드는 부분, 체크판 확인 부분 나누기

import sys

# 체크판 확인
def check_chess(arr, s_color):
    cnt = 0
    for r in range(8):
        for c in range(8):
            # 짝수칸일 경우 : 처음이랑 같아야 맞음, 아니면 증가
            if (r + c) % 2 == 0:
                if arr[r][c] != s_color:
                    cnt += 1
            # 홀수칸일 경우 : 달라야 맞음
            else:
                if arr[r][c] == s_color:
                    cnt += 1
    return cnt

M, N = map(int, sys.stdin.readline().split())

arr = [list(sys.stdin.readline().strip()) for _ in range(M)]

min_cnt = float('inf')

for R in range(M - 8 + 1):
    for C in range(N - 8 + 1):
        # 8 * 8 체스판 만들기
        new_arr = [row[C:C+8] for row in arr[R:R+8]]
        # 함수 2번 돌리는 이유 : 시작이 먼지 알 수 없으므로
        cnt_B = check_chess(new_arr, 'B')
        cnt_W = check_chess(new_arr, 'W')
        # 최소값
        min_cnt = min(min_cnt, cnt_B, cnt_W)

print(min_cnt)