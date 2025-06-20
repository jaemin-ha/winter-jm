# 병사 관리
# 병사 : 고유 번호, 소속팀, 평판 점수
# 고유번호(1 ~ 100000), 팀(1 ~ 5), 평판(1 ~ 5)
# 프로그램을 제작

# 기능
# 1. 병사 고용
# 2. 병사 해고
# 3. 평판 점수 변경
# 4. 특정 팀 선수들 평판 일괄 변경
# 5. 특정 팀 선수 중 제일 높은 사람 탐색

# 초기화 함수
def init():
    global people
    # 담을 리스트
    people = []

# 1. 고용
def hire(ID, Team, score):
    # 추가
    people.append([ID, Team, score])

# 2. 해고
def fire(ID):
    for i in people:
        if i[0] == ID:
            people.remove(i)

# 3. ID로 평판 점수 변경
def updateSoldier(ID, score):
    for i in people:
        if i[0] == ID:
            i[2] = score

# 4. 특정 팀 점수를 변경
def updateTeam(Team, change_score):
    for i in people:
        if i[1] == Team:
            # 계산 과정
            cal_score = i[2] + change_score
            # 5 초과 시 5로 설정
            if cal_score > 5:
                i[2] = 5
            # 1 미만 시 1로 설정
            elif cal_score < 1:
                i[2] = 1
            else:
                i[2] = cal_score

# 5. 특정 팀 중 제일 높은 사람
def bestSoldier(Team):
    max_v = 0
    max_soldier = 0
    for i in people:
        if i[1] == Team:
            # 클 경우
            if max_v < i[2]:
                max_v = i[2]
                max_soldier = i[0]
            # 같을 경우 고유 번호 큰 걸로 갱신
            elif max_v == i[2] and max_soldier < i[0]:
                max_soldier = i[0]

    return max_soldier

people = []

print(people)


# 느낀 점 기록
# 25_06_20
# 시간 최적화를 못해서 일단 개선해야 할 필요성이 존재함
# 추후 연결 리스트 습득 후 개선 예정