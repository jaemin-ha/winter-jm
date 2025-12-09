# 백준 2501 약수 구하기
# N이 10000이라서 그냥 구함

N, K = map(int, input().split())

# 약수 넣을 리스트
lst = []

for i in range(1, N+1):
    if N % i == 0:
        lst.append(i)

# 약수개수가 K보다 적으면 0 출력
if len(lst) < K:
    print(0)
else:
    print(lst[K-1])