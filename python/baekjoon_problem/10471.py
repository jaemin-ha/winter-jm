# 백준 10471 공간을 만들어 봅시다

W, P = map(int, input().split())
partions = list(map(int, input().split()))

# 0과 폭 추가
partions.append(0)
partions.append(W)

result = []

for i in range(P+2):
    for j in range(i, P+2):
        result.append(abs(partions[i]-partions[j]))

new_result = list(set(result))
# 순서 보장 X -> 정렬 시키기
new_result.sort()

print(*new_result[1:])