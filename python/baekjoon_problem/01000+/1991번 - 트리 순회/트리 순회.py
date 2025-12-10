import sys
input = sys.stdin.readline

N = int(input())
tree = {}
for _ in range(N):
    node, l, r = input().split()
    tree[node] = [l, r]

# 전위 순회
def preorder(root):
    if root != '.':
        print(root, end='')
        preorder(tree[root][0])
        preorder(tree[root][1])

# 중위 순회
def inorder(root):
    if root != '.':
        inorder(tree[root][0])
        print(root, end='')
        inorder(tree[root][1])

# 후위 순회
def postorder(root):
    if root != '.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end='')

# 줄 바꿈을 위해서 print()
preorder('A')
print()
inorder('A')
print()
postorder('A')