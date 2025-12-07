# 백준 10551 STROJOPIS

# 키보드 정리
lst_1 = ["1", "Q", "A", "Z"]
lst_2 = ["2", "W", "S", "X"]
lst_3 = ["3", "E", "D", "C"]
lst_4 = ["4", "5", "R", "T", "F", "G", "V", "B"]
lst_5 = ["6", "7", "Y", "U", "H", "J", "N", "M"]
lst_6 = ["8", "I", "K", ","]
lst_7 = ["9", "O", "L", "."]
lst_8 = ["0", "-", "=", "P", "[", "]", ";", "'", "/"]

# 결과
result = [0] * 8

string = input()

# 분류
for s in string:
    if s in lst_1:
        result[0] += 1
    elif s in lst_2:
        result[1] += 1
    elif s in lst_3:
        result[2] += 1
    elif s in lst_4:
        result[3] += 1
    elif s in lst_5:
        result[4] += 1
    elif s in lst_6:
        result[5] += 1
    elif s in lst_7:
        result[6] += 1
    elif s in lst_8:
        result[7] += 1

for i in range(8):
    print(result[i])