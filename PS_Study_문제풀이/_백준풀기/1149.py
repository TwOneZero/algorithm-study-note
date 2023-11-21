n = int(input())

dp = [list(map(int, input().split())) for _ in range(n)]

#
# dp(1, 0) -> min(dp(0, 1), dp(0, 2)) + rgb(1, 0)
# dp(1, 1) -> min(dp(0, 0), dp(0, 2)) + rgb(1, 1)
# dp(1, 2) -> min(dp(0, 0), dp(0, 1)) + rgb(1, 2)
#

for i in range(1, n):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + dp[i][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + dp[i][1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + dp[i][2]

# 마지막 꺼 최소
print(min(dp[-1]))
