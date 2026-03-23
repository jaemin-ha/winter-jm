# 백준 10409 서버
n, T = map(int, input().split())
nums = list(map(int, input().split()))

# 아예 일이 수행 못하는 경우를 생각해 -1로 설정
result = -1

for i in range(n):
    T -= nums[i]

    if T < 0:
        break

    result = i

print(result+1)