### 백준 2747 피보나치 수 
## 1초

import sys

n = int(input())

# 45까지
dp = [0] * 46

# DP Bottom-Up 방식
def fibo(n):
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]
    
print(fibo(n))