# 정답 확인 용

def init():
    global people
    people = []

def hire(ID, Team, score):
    people.append([ID, Team, score])

def fire(ID):
    for i in people:
        if i[0] == ID:
            people.remove(i)

def updateSoldier(ID, score):
    for i in people:
        if i[0] == ID:
            i[2] = score

def updateTeam(Team, change_score):
    for i in people:
        if i[1] == Team:
            cal_score = i[2] + change_score
            if cal_score > 5:
                i[2] = 5
            elif cal_score < 1:
                i[2] = 1
            else:
                i[2] = cal_score

def bestSoldier(Team):
    max_v = 0
    max_soldier = 0
    for i in people:
        if i[1] == Team:
            if max_v < i[2]:
                max_v = i[2]
                max_soldier = i[0]
            elif max_v == i[2] and max_soldier < i[0]:
                max_soldier = i[0]

    return max_soldier

# 소스코드와 같은 디렉토리에 input.txt 파일을 생성해서 거기에 입력을 넣은 뒤 아래 주석을 지우면 편하게 실행 가능합니다 :)
fs = open("input.txt", "r")
input = fs.readline

CMD_INIT = 1
CMD_HIRE = 2
CMD_FIRE = 3
CMD_UPDATE_SOLDIER = 4
CMD_UPDATE_TEAM = 5
CMD_BEST_SOLDIER = 6

def run():
    isCorrect = False
    numQuery = int(input())

    for i in range(numQuery):
        line = list(map(int, input().split()))
        cmd = line[0]

        if cmd == CMD_INIT:
            init()
            isCorrect = True
        elif cmd == CMD_HIRE:
            mID, mTeam, mScore = line[1], line[2], line[3]
            hire(mID, mTeam, mScore)
        elif cmd == CMD_FIRE:
            mID = line[1]
            fire(mID)
        elif cmd == CMD_UPDATE_SOLDIER:
            mID, mScore = line[1], line[2]
            updateSoldier(mID, mScore)
        elif cmd == CMD_UPDATE_TEAM:
            mTeam, mChangeScore = line[1], line[2]
            updateTeam(mTeam, mChangeScore)
        elif cmd == CMD_BEST_SOLDIER:
            mTeam = line[1]
            userAns = bestSoldier(mTeam)
            ans = line[2]
            if userAns != ans:
                isCorrect = False
        else:
            isCorrect = False

    return isCorrect

T, MARK = map(int, input().split())

for tc in range(1, T + 1):
    score = MARK if run() else 0
    print(f'#{tc} {score}')
