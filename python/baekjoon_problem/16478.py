# 백준 16478 원의 분할

a, b, c = map(int, input().split())

# 만나는 점 기준으로 이런 공식이 성립함
# 닮음을 사용
# pab * pcd = pbc * pda

print(a*c / b)