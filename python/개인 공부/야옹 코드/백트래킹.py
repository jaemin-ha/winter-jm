# 야옹 강의 <백트래킹>
# n중 반복문 구현하기

# n자리 m진수 => m개 중 n개 고르기
n = int(input())
m = int(input())

# 몇 자리인지
arr = [0] * n


# 1. 중복 순열
def recur1(depth):
    # 종료 조건
    if depth == n:
        print(*arr)
        return

    # 반복문
    for i in range(m):
        arr[depth] = i
        recur1(depth+1)

recur1(0)

# 2. 순열
def recur2(depth):
    # 종료 조건
    if depth == n:
        print(*arr)
        return

    # 반복문
    for i in range(m):
        if visited[i]:
            continue
        arr[depth] = i
        visited[i] = True
        recur1(depth+1)
        visited[i] = False

# 방문 처리 배열 생성 -> 순열
# 같은 인덱스를 안 고르는
visited = [0] * m

recur2(0)


# 3. 조합
def recur3(depth, prv):
    # 종료 조건
    if depth == n:
        print(*arr)
        return

    # 반복문
    for i in range(prv, m):
        arr[depth] = i
        recur3(depth+1, i+1)

recur3(0, 0)


# 고르는 과정을 o, x로 표현 : 3이랑 같은데 다른 방식
def recur4(idx, cnt):
    if cnt == n:
        print(*arr)
        return

    if idx == m:
        return

    arr[cnt] = idx
    # 고를 때
    recur4(idx + 1, cnt + 1)

    # 안 고를 떄
    recur4(idx + 1, cnt)

recur4(0, 0)