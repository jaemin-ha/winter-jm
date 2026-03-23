# 백준 26264 빅데이터? 정보보호!

N = int(input())

string = input()

cnt1 = 0
cnt2 = 0

for i in range(len(string)):
    if string[i] == "s":
        cnt1 += 1
    elif string[i] == "b":
        cnt2 += 1

if cnt1 > cnt2:
    print("security!")
elif cnt1 == cnt2:
    print("bigdata? security!")
else:
    print("bigdata?")