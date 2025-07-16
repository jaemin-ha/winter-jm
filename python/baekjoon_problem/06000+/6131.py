### 백준 6131 완전 제곱 수
##  1초

##  아이디어 : A, B 제한이 500까지이므로,
##  반복문을 엄청 많이 하지 않는다면 상관 없다고 생각

N = int(input())

# 결과 리스트
lst = []

for i in range(1, 500):
    a = i ** 2
    for j in range(1, i+1):
        b = j ** 2
        # 판단
        if a == b + N:
            lst.append([i, j])


print(len(lst))