### 백준 3584 가장 가까운 공통 조상
### 1초

### 트리, 최소 공통 조상 -> 깊이를 고려해야 함

import sys
input = sys.stdin.readline

# 루트 노드를 다 구하기
def find(node):
    result = [node]

    while tree[node]:
        result.append(tree[node])
        node = tree[node]
    # 배열 반환
    return result

# 테스트 케이스
T = int(input())

for tc in range(1, T+1):
    # 노드의 수
    N = int(input())

    # 트리 기본 틀
    tree = [0] * (N+1)
    
    # tree 제작
    for _ in range(N-1):
        A, B = map(int, input().split())
        tree[B] = A

    # 마지막 줄은 결과값 구하기
    a, b = map(int, input().split())

    # 깊이 확인
    i, j = 0, 0

    # 배열 반환
    x = find(a)
    y = find(b)

    # 깊이(배열 길이)에 따라 깊이 같게 만들기
    if len(x) > len(y):
        i += len(x) - len(y)
    
    elif len(y) > len(x):
        j += len(y) - len(x)
    
    # 값 다르면 1추가 해서 다시 비교
    while x[i] != y[j]:
        i += 1
        j += 1
    
    print(x[i])