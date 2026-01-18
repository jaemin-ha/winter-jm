# 백준 30402 감마선을 맞은 컴퓨터

photo = [list(input().split()) for _ in range(15)]

for i in range(15):
    if "w" in photo[i]:
        print("chunbae")
        break

    elif "b" in photo[i]:
        print("nabi")
        break

    elif "g" in photo[i]:
        print("yeongcheol")
        break