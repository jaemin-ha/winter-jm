# 백준 2846 오르막길

N = int(input())

nums = list(map(int, input().split()))

max_v = 0

for i in range(N):
    lst = [nums[i]]

    # 다음 숫자들을 비교 -> 오르막인지
    for j in range(i+1, N):
        if nums[j-1] < nums[j]:
            lst.append(nums[j])

        # 아니면 종료
        else:
            break

    s = max(lst) - min(lst)

    # 최대 오르막 길이
    if max_v < s:
        max_v = s

print(max_v)