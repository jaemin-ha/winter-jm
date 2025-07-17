N = int(input())

lst = []

younghun = 1

namgyu = younghun + 2

taehwi = N - (younghun + namgyu)

total = younghun + namgyu + taehwi

while total <= N:
    if taehwi == 0:
        break

    if taehwi >= 2 and taehwi % 2 == 0:
        lst.append([younghun, namgyu, taehwi])

    younghun += 1

    namgyu = younghun + 2

    taehwi = N - (younghun + namgyu)

    total = younghun + namgyu + taehwi

print(len(lst))