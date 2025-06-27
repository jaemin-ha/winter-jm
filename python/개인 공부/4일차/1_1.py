# 높이가 4이므로 16개의 배열 만들기
tree = [0] * 16

tree[1] = 'A'
tree[2] = 'B'
tree[3] = 'C'
tree[4] = 'D'
tree[5] = 'E'
tree[7] = 'F'
tree[10] = 'G'

# 재귀 호출
# 파라미터 : 관리해야할 값 또는 누적값
def dfs(n):
    # 1. 종료조건 (정점 범위가 넘어갈 때 종료)
    if n > 16:
        return 0

    # 가지치기
    if tree[n] == 0:
        return 0

    # 2. 재귀호출 (가지 수만큼 호출)
    # 왼쪽
    left = dfs(n * 2)
    # 오른쪽
    right = dfs(n * 2 + 1)

    return left + right + 1

print(dfs(1))