# 백준 32369 양파 실험

N, A, B = map(int, input().split())

good_onion = 1
bad_onion = 1

current = 0

while current < N:
    current += 1
    good_onion += A
    bad_onion += B

    # 비난 양파가 크면 둘이 바꿈
    if good_onion < bad_onion:
        good_onion, bad_onion = bad_onion, good_onion

    # 같다면 비난 양파 자름
    elif good_onion == bad_onion:
        bad_onion -= 1


print(good_onion, bad_onion)