n = int(input())

# dp -> 1이 되게하는 최소한의 연산 횟수

dp = [0] * (n + 1)

dp[1] = 0

for i in range(2, n + 1):
    # 1을 빼는 경우
    dp[i] = dp[i - 1] + 1
    # 3을 나누는 경우
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
    # 2를 나누는 경우
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)

print(dp[n])

