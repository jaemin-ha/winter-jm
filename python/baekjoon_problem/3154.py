### 백준 3154 알람시계
##  1초
##  아이디어 : 문제를 잘못 이해해서 키패드 거리를 계산해야 하는데
##  그냥 거리로 계산해서 원하는 정답이 안 나옴
##  0이나 한자리 숫자를 입력받을 경우를 고려안함
#   -> 너무 코드가 복잡해져서 2자리로 넣는 방법을 찾아서 적용

# 키패드 별 좌표
key = {'1': (0, 0), '2': (1, 0), '3': (2, 0),
       '4': (0, 1), '5': (1, 1), '6': (2, 1),
       '7': (0, 2), '8': (1, 2), '9': (2, 2),
       '0': (1, 3)}

# 노력 계산
def effort(H, M):
    # 하나의 리스트로 만들기 -> [0, 0, 1, 1]
    cal = list(H) + list(M)

    efforts = 0

    for k in range(3):
        x1, y1 = key[cal[k]]
        x2, y2 = key[cal[k + 1]]
        efforts += abs(x1 - x2) + abs(y1 - y2)

    return efforts

# 입력
time = input()

hour = int(time[0:2])
minute = int(time[3:5])

hours = []
minutes = []

while hour < 100:
    # 2자리로 넣기
    hours.append(f'{hour:02}')
    hour += 24

while minute < 100:
    # 2자리로 넣기
    minutes.append(f'{minute:02}')
    minute += 60

# 출력
result = float('inf')
result_hour = ''
result_minute = ''

# 함수 처리
for i in hours:
    for j in minutes:
        if result > effort(i, j):
            result = effort(i, j)
            result_hour = i
            result_minute = j

print(f'{result_hour}:{result_minute}')