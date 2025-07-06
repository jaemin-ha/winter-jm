### 백준 9085 더하기
##  1초

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))

    print(sum(nums))