import sys
input = sys.stdin.readline

dict = {
    'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5,
    'f' : 6, 'g' : 7, 'h' : 8, 'i' : 9, 'j' : 10,
    'k' : 11, 'l' : 12, 'm' : 13, 'n' : 14, 'o' : 15,
    'p' : 16, 'q' : 17, 'r' : 18, 's' : 19, 't' : 20,
    'u' : 21, 'v' : 22, 'w' : 23, 'x' : 24, 'y' : 25,
    'z' : 26
}

L = int(input())
string = list(input())

cnt = 0

for i in range(L):  
    cnt += dict[string[i]] * (31**i)

# L이 커지면 너무 커지는 경우 고려
# 그냥 cnt가 아니라 1234567891로 나누는 걸 표시
print(cnt % 1234567891)