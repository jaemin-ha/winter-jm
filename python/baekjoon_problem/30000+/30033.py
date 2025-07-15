### 백준 30033 Rust Study
##  1초


N = int(input())

plan = list(map(int, input().split()))

actual = list(map(int, input().split()))

cnt = 0

for i in range(N):
    if actual[i] >= plan[i]:
        cnt += 1


print(cnt)