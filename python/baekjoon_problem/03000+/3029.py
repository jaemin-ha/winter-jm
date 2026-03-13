# 백준 3029 경고

current = input()
sodium = input()

h1 = int(current[0:2])
m1 = int(current[3:5])
s1 = int(current[6:8])

h2 = int(sodium[0:2])
m2 = int(sodium[3:5])
s2 = int(sodium[6:8])

if s2 < s1:
    s2 += 60
    m2 -= 1

if m2 < m1:
    m2 += 60
    h2 -= 1

if h2 < h1:
    h2 += 24

a = str(h2 - h1)
b = str(m2 - m1)
c = str(s2 - s1)

if len(a) == 1:
    a = "0" + a

if len(b) == 1:
    b = "0" + b

if len(c) == 1:
    c = "0" + c

# 이 부분을 고려해야함 -> 문제에서 적어도 1초 기다리므로
if current == sodium:
    print("24:00:00")
else:
    print(f"{a}:{b}:{c}")