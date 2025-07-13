### 백준 11800 Tawla
##  3초

T = int(input())

nums_dict = {
    1 : 'Yakk',
    2: 'Doh',
    3: 'Seh',
    4: 'Ghar',
    5: 'Bang',
    6: 'Sheesh'
}

for tc in range(1, T+1):
    nums = list(map(int, input().split()))
    
    # 큰 거 부터 나타냄
    nums.sort(reverse=True)
    
    # 판단 과정
    if nums[0] == nums[1]:
        if nums[0] == 1:
            print(f'Case {tc}: Habb Yakk')
        elif nums[0] == 2:
            print(f'Case {tc}: Dobara')
        elif nums[0] == 3:
            print(f'Case {tc}: Dousa')
        elif nums[0] == 4:
            print(f'Case {tc}: Dorgy')
        elif nums[0] == 5:
            print(f'Case {tc}: Dabash')
        else:
            print(f'Case {tc}: Dosh')
    else:
        if nums[0] + nums[1] == 11:
            print(f'Case {tc}: Sheesh Beesh')
        else:
            print(f"Case {tc}: {nums_dict[nums[0]]} {nums_dict[nums[1]]}")

