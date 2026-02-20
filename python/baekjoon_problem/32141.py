# 백준 32141 카드 게임 (Easy)

N, H = map(int, input().split())
nums = list(map(int, input().split()))

new_lst = [0] * N

new_lst[0] = nums[0]

for i in range(1, N):
    new_lst[i] = nums[i] + new_lst[i-1]

if sum(nums) < H:
    print(-1)

else:
    for i in range(N):
        if new_lst[i] >= H:
            print(i+1)
            break