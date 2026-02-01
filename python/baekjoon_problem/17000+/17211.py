# 백준 17211 좋은 날 싫은 날
# 이전 값을 기억해서 확률을 곱해가는 문제

N, start = map(int, input().split())
probability = list(map(float, input().split()))

# 처음 날에 대한 분기
if start == 0:
    g = probability[0]
    b = probability[1]

else:
    g = probability[2]
    b = probability[3]

# (날짜-1) 만큼 반복
for i in range(N-1):
    good = g
    bad = b

    # 좋을 날일 확률
    g = (good * probability[0]) + (bad * probability[2])
    # 나쁜 날일 확률
    b = (good * probability[1]) + (bad * probability[3])


result = int(g*1000)

print(result)
print(1000-result)