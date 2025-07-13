### 백준 25495 에어팟
##  1초

##  문제를 제대로 이해하지 못해 시간이 너무 오래걸린거 같다.
##  내가 이해를 못한건가 -> 아니면 반례?

N = int(input())
phone = list(map(int, input().split()))

# 이전 휴대폰
next = -1

# 현재 배터리 사용량
battery = 0

# 연속 시 필요
basic = 1

for i in range(N):
    # 다르다면
    if phone[i] != next:
        # 추가하고, 연속 시 필요 값 초기화
        battery += 2
        basic = 2

    else:
        # 같다면, 배터리 추가해주고, 필요 값 2배하기
        battery += 2 * basic
        basic *= 2

    # 다음 반복 시 비교할 값 갱신
    next = phone[i]

    # 100이상 시, 배터리 초기화, 휴대폰 초기화, 필요 값 1로
    if battery >= 100:
        battery = 0
        next = -1
        basic = 1

print(battery)