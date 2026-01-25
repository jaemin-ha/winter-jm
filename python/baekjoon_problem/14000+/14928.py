# 백준 14928 큰 수 (BIG)

month = int(input())
day = int(input())

if month > 2:
    print("After")

elif month == 1:
    print("Before")

else:
    if day < 18:
        print("Before")

    elif day > 18:
        print("After")

    else:
        print("Special")