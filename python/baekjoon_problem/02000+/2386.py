# 백준 2386 도비의 영어 공부

while True:
    string = input()

    alphabet = string[0]
    munjang = string[2:]

    cnt = 0

    # 종료 조건
    if alphabet == "#":
        break

    # 타겟이라면 추가
    for i in munjang:
        if i.lower() == alphabet:
            cnt += 1

    # 출력
    print(alphabet, cnt)