# 백준 11005 진법 변환 2
# 진법 변환하는 원리를 알아야 푸는 듯

N, B = map(int, input().split())

# 진법 변환 나머지 (0 ~ 35)
number = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# 결과값
s = ''

# 진법 변환이 진법에 해당하는 숫자로 나누고 나머지를 뒤집는 원리
# N이 0이 될떄까지 나누기 (1이어도 나누면 되니까)
while N:
    # 나머지를 추가
    s += number[N % B]
    # 나누기
    N //= B

print(s[::-1])