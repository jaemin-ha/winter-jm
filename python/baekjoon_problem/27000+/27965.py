# 백준 27965 N결수
# 1 : 문자열 추가한다음 제출 -> 역시나 시간초과
# 2 : 고민해봤는데 방법이 생각이 안났음
# -> 서칭하니 밑에와 같은 방식으로 수를 만드는 거였음 (넘나 어려운거)

N, K = map(int, input().split())

remain = ""

for i in range(1, N+1):
    # 수를 추가하고
    remain += str(i)

    # 그 나머지를 구해서 반영
    remain = str(int(remain) % K)

print(int(remain))