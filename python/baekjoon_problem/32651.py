# 백준 32651 인간은 무엇인가

N = int(input())

if N > 100000:
    print("No")
else:
    if N % 2024 == 0:
        print("Yes")
    else:
        print("No")