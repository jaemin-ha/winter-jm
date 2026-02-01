# 백준 34552 디딤돌 장학금

money = list(map(int, input().split()))

N = int(input())

result = 0
for i in range(N):
    i, score, subject = input().split()

    # 17학점이상, 평점 2.0이상
    if float(score) >= 2.0 and int(subject) >= 17:
        result += money[int(i)]

print(result)