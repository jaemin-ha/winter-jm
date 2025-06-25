### DP 공부

## 재귀 함수
def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

result = fibo(10)

print(result)


## 1. Bottom-Up 방식

def dp_fib1(n):
    # 미리 배열 선언
    dp = [0] * (n + 1)

    dp[0] = 0
    dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

print(dp_fib1(100))


## 2. Top-Down 방식

# 메모이제이션용 dp 배열 (모든 값을 -1로 초기화)
dp = [-1] * 100

def dp_fib2(n):
    if n <= 1:
        return n

    if dp[n] != -1:  # 이미 계산한 값이면 바로 반환
        return dp[n]

    dp[n] = dp_fib2(n - 1) + dp_fib2(n - 2)
    return dp[n]

print(dp_fib2(20))