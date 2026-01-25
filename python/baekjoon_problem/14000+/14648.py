# 백준 14648 쿼리 맛보기
# q가 10000이어서 크게 생각 안함

n, q = map(int, input().split())

nums = list(map(int, input().split()))

for _ in range(q):
    order = list(map(int, input().split()))
    
    # order에 따른 구분
    if order[0] == 1:
        print(sum(nums[order[1]-1:order[2]-1+1]))
        nums[order[1]-1], nums[order[2]-1] = nums[order[2]-1], nums[order[1]-1]

    else:
        s = sum(nums[order[1]-1:order[2]-1+1]) - sum(nums[order[3]-1:order[4]-1+1])
        print(s)