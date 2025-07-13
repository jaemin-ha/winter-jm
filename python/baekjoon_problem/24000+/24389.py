# 백준 2의 보수

N = int(input())

# 32비트로 변환 (F:4개 -> 8개 -> 32)
N_32 = N & 0xFFFFFFFF

# N의 보수 -> 반전시키고 + 1
complement = (~ N + 1) & 0xFFFFFFFF

# XOR 연산을 통해 다르면 1, 같으면 0으로 연산
result = N_32 ^ complement

# 1의 개수 세기
cnt = bin(result).count('1')

print(cnt)