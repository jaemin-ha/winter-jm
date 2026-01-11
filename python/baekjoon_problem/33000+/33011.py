# 백준 33011 홀수와 짝수 게임
# 숫자가 작아서 원리만 이해하면 풀 수 있었음

T = int(input())

for tc in range(T):
    N = int(input())
    nums = list(map(int, input().split()))

    # 홀수
    cnt1 = 0

    # 짝수
    cnt2 = 0

    for i in range(N):
        if nums[i] % 2 == 1:
            cnt1 += 1
        else:
            cnt2 += 1

    # 같으면 희원 승
    if cnt1 == cnt2:
        print("heeda0528")

    else:
        # 어느 한쪽이 큰데 홀수면 채완 승
        if max(cnt1, cnt2) % 2 == 1:
            print("amsminn")
        # 짝수면 희원승
        else:
            print("heeda0528")