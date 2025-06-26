arr = [225, 220, 160, 160, 160, 100]

# 내림 차순 정렬
arr.sort(reverse=True)

def lower_bound(target):
    s = 0
    e = len(arr) - 1
    answer = -1

    while s <= e:
        mid = (s + e) // 2

        # 역순 정렬 고려
        if arr[target] >= arr[mid]:
            e = mid - 1
            answer = mid

        else:
            s = mid + 1

    print(f'{target+1}등: {arr[answer]}~{arr[answer-1]-1}')


for i in range(2, 7):
    lower_bound(i-1)

