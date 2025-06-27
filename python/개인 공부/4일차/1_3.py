# 세그먼트 트리 만들기
arr = [0, 1000, 3000, 1000, 500, 1000, 2000, 800, 1000]

# 배열의 크기를 4N으로 만들면 안전하게 만들 수 있다. (암기해야 편함)
# 최악의 경우를 생각해보기 -> 8개말고, 더 늘어날 수 있음
segTree = [0] * (4 * len(arr))

# 파라미터 : 현재 인덱스와 바라보고 있는 범위의 시작 / 끝
def makeSeg(n, s, e):

    # 기저 조건 : 리프 노드일 때 (리프 노드를 판단해야함)
    if s == e:
        segTree[n] = arr[s]
        return segTree[n]

    # 좌우로 내려가는 코드
    mid = (s + e) // 2

    # 왼쪽
    left = makeSeg(n * 2, s, mid)

    # 오른쪽
    right = makeSeg(n * 2 + 1, mid + 1, e)

    segTree[n] = min(left, right)
    # segTree[n] = max(left, right)
    # segTree[n] = left + right

    return segTree[n]

makeSeg(1, 1, len(arr) - 1)

print(segTree)