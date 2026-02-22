# 백준 15873 공백 없는 A+B

A = input()

if len(A) == 2:
    B = int(A[0])
    C = int(A[1])

elif len(A) == 3:
    if A[1] == "0":
        B = int(A[0:2])
        C = int(A[2])
    else:
        B = int(A[0])
        C = int(A[1:3])

else:
    B = int(A[0:2])
    C = int(A[2:4])

print(B + C)