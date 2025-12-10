import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

# 트리에 저장하기 : 자식들을 부모리스트에 저장
tree = [[] for _ in range(N)]

# 루트를 저장해놓아야함 -> 루트가 제거될수도 있으니
root = -1

for i in range(N):
    if nums[i] == -1:
        root = i
    else:
        tree[nums[i]].append(i)

# 제거할 노드
r_node = int(input())

def dfs(x):
    # 제거된 노드면 리프 아님
    if x == r_node:
        return 0
    
    cnt = 0
    child_cnt = 0

    for c in tree[x]:
        if c != r_node:
            child_cnt += 1
            cnt += dfs(c)
    
    # child_cnt가 0이 아니라면 자식이 존재
    if child_cnt != 0:
        return cnt
    # 자식이 없으면 그 노드가 리프 노드
    else:
        return 1

if root == r_node:
    print(0)
else:
    print(dfs(root))

