# 백준 2535 아시아 정보올림피아드

N = int(input())

lst = []

for _ in range(N):
    country, person, score = map(int, input().split())
    lst.append([country, person, score])

# 내림차순으로 정렬
lst.sort(key=lambda x: -x[2])

# 메달 개수 2개까지만
select_country = []
# 결과
result = []

# 국가 개수를 계산하여 개수가 2개 이하만 추가
for i in range(N):
    if len(result) == 3:
        break

    if select_country.count(lst[i][0]) < 2:
        select_country.append(lst[i][0])
        result.append(lst[i])


for i in range(3):
    print(result[i][0], result[i][1])