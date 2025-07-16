### 백준 34001 임스의 일일 퀘스트
##  1초

##  아이디어 : 그냥 조건식 나누는게 나을 것 같다고 생각

L = int(input())

acain = [0, 0, 0, 0, 0, 0]
grandis = [0, 0, 0, 0, 0, 0, 0]

# 아케인 분류
if 200 <= L < 210:
    acain[0] = 500
elif 210 <= L < 220:
    acain[0] = 300
    acain[1] = 500
elif 220 <= L < 225:
    acain[0] = 100
    acain[1] = 300
    acain[2] = 500
elif 225 <= L < 230:
    acain[0] = 100
    acain[1] = 100
    acain[2] = 300
    acain[3] = 500
elif 230 <= L < 235:
    acain[0] = 100
    acain[1] = 100
    acain[2] = 100
    acain[3] = 300
    acain[4] = 500
elif 235 <= L < 245:
    acain[0] = 100
    acain[1] = 100
    acain[2] = 100
    acain[3] = 100
    acain[4] = 300
    acain[5] = 500
elif 245 <= L < 250:
    acain[0] = 100
    acain[1] = 100
    acain[2] = 100
    acain[3] = 100
    acain[4] = 100
    acain[5] = 300
else:
    acain[0] = 100
    acain[1] = 100
    acain[2] = 100
    acain[3] = 100
    acain[4] = 100
    acain[5] = 100

# 그란디스 분류
if 260 <= L < 265:
    grandis[0] = 500
elif 265 <= L < 270:
    grandis[0] = 300
    grandis[1] = 500
elif 270 <= L < 275:
    grandis[0] = 100
    grandis[1] = 300
    grandis[2] = 500
elif 275 <= L < 280:
    grandis[0] = 100
    grandis[1] = 100
    grandis[2] = 300
    grandis[3] = 500
elif 280 <= L < 285:
    grandis[0] = 100
    grandis[1] = 100
    grandis[2] = 100
    grandis[3] = 300
    grandis[4] = 500
elif 285 <= L < 290:
    grandis[0] = 100
    grandis[1] = 100
    grandis[2] = 100
    grandis[3] = 100
    grandis[4] = 300
    grandis[5] = 500
elif 290 <= L < 295:
    grandis[0] = 100
    grandis[1] = 100
    grandis[2] = 100
    grandis[3] = 100
    grandis[4] = 100
    grandis[5] = 300
    grandis[6] = 500
elif 295 <= L < 300:
    grandis[0] = 100
    grandis[1] = 100
    grandis[2] = 100
    grandis[3] = 100
    grandis[4] = 100
    grandis[5] = 100
    grandis[6] = 300
elif L == 300:
    grandis[0] = 100
    grandis[1] = 100
    grandis[2] = 100
    grandis[3] = 100
    grandis[4] = 100
    grandis[5] = 100
    grandis[6] = 100

print(*acain)
print(*grandis)