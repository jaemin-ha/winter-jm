# 백준 1966 프린터 큐
# 문제에 큐를 사용하는 것이 명확한 문제

from collections import deque

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    q = deque(nums)
    # 뽑는 횟수 세기
    cnt = 0

    while q:
        # 최대값
        max_v = max(q)

        # 맨 왼쪽 숫자
        f = q.popleft()

        # 뽑으니 크기 1감소
        M -= 1

        # 뽑은 숫자가 최대면
        if max_v == f:
            cnt += 1

            # M이 음수면 뽑은 것이 찾는 숫자
            if M < 0:
                print(cnt)
                break

        # 제일 큰 게 아니면
        else:
            # 다시 추가
            q.append(f)

            # 맨 앞이면 다시 맨 뒤로 자리 계산
            if M < 0:
                M = len(q) - 1