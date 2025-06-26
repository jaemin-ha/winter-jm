# 학생 수
student = [207, 200, 100]

# 합격자 명단
arr = [100, 200, 201, 204, 208, 304, 305]

# 이진 탐색
def bs(n):
    s = 0
    e = len(arr) - 1

    while s <= e:
        mid = (s + e) // 2
        
        # 찾는 경우
        if arr[mid] == n:
            return 1

        if arr[mid] > n:
            e = mid - 1

        else:
            s = mid + 1
            
    # 찾지 못할 경우       
    return 0

# 합격자 수
cnt = 0

for i in range(len(student)):
    if bs(student[i]):
        cnt += 1

print(cnt)