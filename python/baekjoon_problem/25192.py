### 백준 25192 인사성 밝은 곰곰이
##  1초 이내

N = int(input())

# 결과
result = 0

# 중복을 없애려고 set
people = set()

# N번 반복
for _ in range(N):
    name = input()
    
    # ENTER인 경우, 결과값 더하고, people 초기화
    if name == 'ENTER':
        result += len(people)
        people = set()
    
    # 아니라면 추가
    else:
        people.add(name)

# 마지막에 들어있는 사람들도 추가
result += len(people)

print(result)