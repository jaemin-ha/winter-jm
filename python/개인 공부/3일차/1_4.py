# 츄러스 길이
arr = [50, 30, 40]

# 사람 수
n = 5

# 최대 길이
ans = 0

# 완전 탐색 풀이 -> 첨에 생각한 풀이
for i in range(1, max(arr) + 1):
    cnt = 0

    for j in range(len(arr)):
        cnt += (arr[j] // i)

    if cnt >= n:
        ans = i

print(ans)


# Parametric Search 풀이

# 정렬하자
arr.sort(reverse=True)


# 확인하는 함수
def check(mid):
    # 조각 개수
    cnt = 0
    
    # 구하는 과정
    for c in arr:
        cnt += c // mid
    
    return cnt >= n

# 실제 값을 구하는
def ps():
    # 1cm 부터 시작
    s = 1

    # 최대 길이
    e = max(arr)

    while s <= e:
        mid = (s + e) // 2

        # 왼쪽을 날림 (결과가 가능이므로)
        if check(mid):
            s = mid + 1
            result = mid
        
        # 오른쪽을 날림(불가능이므로)
        else:
            e = mid - 1

    return result

print(ps())
