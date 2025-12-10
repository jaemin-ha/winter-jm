# 백준 5073 삼각형과 세 변
while True:
    a, b, c = map(int, input().split())

    if a == b == c == 0:
        break

    # 길이 확인
    max_v = max(a, b, c)
    remain = a + b + c - max_v

    # 삼각형 분류
    if remain <= max_v:
        print("Invalid")

    elif a == b == c:
        print("Equilateral")

    elif (a == b and a != c) or (b == c and b != a) or (c == a and c != b):
        print("Isosceles")

    else:
        print("Scalene")