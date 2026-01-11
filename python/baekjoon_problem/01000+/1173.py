# 백준 1173 운동
# 함수를 안쓰고도 가능할 것 같은데 명령어가 생각이 안남 -> exit()를 쓰면 되는듯?
# 그래서 함수 사용해서 처리

def calculate_minute(ex_cnt, current):
    global N, T, R

    # 운동 불가 조건
    if m + T > M:
        return -1

    # 운동하는 데 걸리는 시간
    minute = 0

    # 운동 채울 때까지 반복
    while ex_cnt < N:
        # 제한 심박수보다 작거나 같다면 운동 가능
        if current + T <= M:
            ex_cnt += 1
            minute += 1
            current += T

        # 높으면 휴식 필요
        else:
            minute += 1
            current -= R
            # m보다 심박수가 작아진다면 m으로
            if current < m:
                current = m

    return minute

# 입력
N, m, M, T, R = map(int, input().split())

result = calculate_minute(0, m)
print(result)