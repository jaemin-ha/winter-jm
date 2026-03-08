# 백준 17202 핸드폰 번호 궁합

# 핸드폰 번호
first = input()
second = input()

a = ""

for i in range(8):
    a += first[i]
    a += second[i]


while True:
    if len(a) <= 2:
        break

    b = ""

    for i in range(len(a)-1):
        c = int(a[i]) + int(a[i+1])

        if c >= 10:
            b += str(c)[-1]
        else:
            b += str(c)

    a = b

print(a)