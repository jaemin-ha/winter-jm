# 백준 2755 이번학기 평점은 몇점?

# 1. 반올림이 흔히 알고 있는 반올림과 달라서 새로운 반올림 함수 생각해야함
# 2. 1.5라면 1.50으로 출력되게 출력 형식을 고려해야함

def new_round(n):
    return int(n * 100 + 0.5) / 100

dict = {
    "A+": 4.3, "A0": 4.0, "A-": 3.7,
    "B+": 3.3, "B0": 3.0, "B-": 2.7,
    "C+": 2.3, "C0": 2.0, "C-": 1.7,
    "D+": 1.3, "D0": 1.0, "D-": 0.7,
    "F": 0.0
}

N = int(input())

result = 0
subjects = 0

for _ in range(N):
    subject, num, grade = input().split()

    result += int(num) * dict[grade]
    subjects += int(num)

print(f"{new_round(result / subjects):.2f}")