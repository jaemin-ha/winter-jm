### 백준 25191 치킨댄스를 추는 곰곰이를 본 임스
##  1초

##  아이디어 : 치킨이 적을 경우도 고려해야함

N = int(input())

A, B = map(int, input().split())

possible_chicken = A // 2 + B

if N >= possible_chicken:
    print(possible_chicken)

else:
    print(N)