# 백준 34509 2, 4, 6, 8

lst = []

# 2자리
for i in range(10, 100):
    num = str(i)

    # 숫자 8 없음
    if "8" in list(num):
        continue

    # 뒤집었을 때 4의 배수
    new_num = int(num[::-1])

    if new_num % 4 != 0:
        continue

    # 각 자리 수 합 6 배수
    s = 0

    for j in num:
        s += int(j)

    if s % 6 == 0:
        lst.append(i)
        continue

print(lst.pop())