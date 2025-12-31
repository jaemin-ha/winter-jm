# 백준 1269 대칭 차집합

s1, s2 = map(int, input().split())

set_1 = set(list(map(int, input().split())))
set_2 = set(list(map(int, input().split())))

# 교집합
new_set = set_1 & set_2

n1 = s1 - len(new_set)
n2 = s2 - len(new_set)

print(n1 + n2)