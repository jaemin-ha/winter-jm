# 백준 33963 돈 복사

N = input()
new_n = N
cnt = 0

while True:
    new_n = str(int(new_n) * 2)
    # 자리 수 확인
    if len(new_n) > len(N):
        break

    cnt += 1
    
print(cnt)