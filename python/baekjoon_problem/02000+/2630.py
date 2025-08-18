### 백준 2630 색종이 만들기
### 1초 이내

### 모두 확인하는 함수는 생각 후 구현 완료, 자르는 함수가 생각이 안나서 고민함

import sys
input = sys.stdin.readline

### 모두 1인지, 0인지 확인하는 함수
def check(arr):
    cnt1 = 0
    cnt2 = 0
    for r in range(len(arr)):
        for c in range(len(arr)):
            if arr[r][c] == 1:
                cnt1 += 1
            else:
                cnt2 += 1
    
    # cnt가 arr*2의 개수랑 같으면 모두 같은 색
    if cnt1 == (len(arr) ** 2) or cnt2 == (len(arr) ** 2):
        return True
    else:
        return False


N = int(input())
color_paper = [list(map(int, input().split())) for _ in range(N)]

# 개수 파악
white = 0
blue = 0


# 색종이 개수 더하고, 나누는 함수
def divide(paper):
    global white, blue

    if check(paper):
        # 0이면 흰색
        if paper[0][0] == 0:
            white += 1
        # 1이면 블루
        else:
            blue += 1
        # 이미 색이 결정된 부분을 막기 위해
        return
    
    n = len(paper) // 2
    # 왼쪽 위
    divide([row[:n] for row in paper[:n]])
    
    # 오른쪽 위
    divide([row[n:] for row in paper[:n]])
    
    # 왼쪽 아래
    divide([row[:n] for row in paper[n:]])
    
    # 오른쪽 아래
    divide([row[n:] for row in paper[n:]])

divide(color_paper)

print(white)
print(blue)