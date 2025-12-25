# 백준 7785 회사에 있는 사람

import sys
input = sys.stdin.readline

N = int(input())
company = set()

for _ in range(N):
    person, state = map(str, input().split())

    if state == "enter":
        company.add(person)

    else:
        company.remove(person)

new_company = list(company)
new_company.sort(reverse=True)

for i in range(len(new_company)):
    print(new_company[i])