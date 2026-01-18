# 백준 29766 DKSH 찾기

string = input()

cnt = 0

for i in range(len(string) - 3):
    if string[i:i+4] == "DKSH":
        cnt += 1

print(cnt)