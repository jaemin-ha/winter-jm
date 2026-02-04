# 백준 31833 온데간데없을뿐더러

N = int(input())

A = input().split()
B = input().split()

new_A = ''.join(A)
new_B = ''.join(B)

if int(new_A) >= int(new_B):
    print(int(new_B))
else:
    print(int(new_A))